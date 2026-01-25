from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuizCreateSerializer, QuizDetailSerializer
from ..models import Quiz

class CreateQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = QuizCreateSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        quiz = serializer.save()

        return Response(
            QuizDetailSerializer(quiz).data,
            status=status.HTTP_201_CREATED
        )
    
class QuizListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        quizzes = Quiz.objects.filter(creator=request.user)
        
        serializer = QuizDetailSerializer(quizzes, many=True, context={"remove_timestamps": True})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )