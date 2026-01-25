from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuizCreateSerializer, QuizDetailSerializer, QuizUpdateSerializer
from ..models import Quiz
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

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
    
class QuizDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)

        if quiz.creator != request.user:
            raise PermissionDenied("You do not have permission to access this quiz.")

        serializer = QuizDetailSerializer(
            quiz,
            context={"remove_timestamps": True}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)

        if quiz.creator != request.user:
            raise PermissionDenied("You do not have permission to delete this quiz.")
        
        quiz.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)

        if quiz.creator != request.user:
            raise PermissionDenied("You do not have permission to update this quiz.")

        serializer = QuizUpdateSerializer(
            quiz,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        quiz = serializer.save()

        detail_serializer = QuizDetailSerializer(
            quiz,
            context={"remove_timestamps": True}
        )

        return Response(detail_serializer.data, status=status.HTTP_200_OK)
