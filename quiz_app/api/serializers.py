from rest_framework import serializers
from ..models import Quiz, QuizQuestion, QuizOption
from ..services.youtube import extract_youtube_info, download_audio
from ..services.whisper import transcribe_audio
from ..services.gemini import generate_gemini_response
from ..helper.prompt_loader import load_prompt
from ..helper.gemini_parser import parse_gemini_json

class QuizCreateSerializer(serializers.ModelSerializer):
    url = serializers.CharField(write_only=True)
    class Meta:
        model = Quiz
        fields = ['url']

    def create(self, validated_data):
        video_url = validated_data.pop("url")
        info = extract_youtube_info(video_url)
        quiz = Quiz.objects.create(
            video_url=video_url,
            video_id=info["id"],
            title="",
            description="",
            creator=self.context["request"].user
        )

        audio_path = download_audio(video_url, quiz.video_id)
        transcript = transcribe_audio(audio_path)
        prompt = load_prompt("quiz_questions.txt", TRANSCRIPT=transcript)

        # # For local testing with a static transcript file
        # transcript_path = Path(__file__).resolve().parent.parent / "transcript" / "transcript.txt"
        # transcript = transcript_path.read_text(encoding="utf-8")

        prompt = load_prompt("quiz_questions.txt", TRANSCRIPT=transcript) 
        gemini_response = generate_gemini_response(prompt)
        data = parse_gemini_json(gemini_response)
        quiz.title = data["title"]
        quiz.description = data["description"]
        quiz.save()

        for q in data["questions"]:
            question = QuizQuestion.objects.create(
                quiz=quiz,
                question_title=q["question_title"],
                answer=q["answer"]
            )

            for opt in q["question_options"]:
                QuizOption.objects.create(
                    question=question,
                    text=opt
                )
        return quiz

class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = ["text"]

class QuizQuestionSerializer(serializers.ModelSerializer):
    question_options = serializers.SerializerMethodField()
    class Meta:
        model = QuizQuestion
        fields = [
            "id",
            "question_title",
            "question_options",
            "answer",
            "created_at",
            "updated_at",
        ]

    def get_question_options(self, obj):
        return [opt.text for opt in obj.question_options.all()]

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
            "video_url",
            "questions",
        ]