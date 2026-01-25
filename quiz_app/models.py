from django.db import models

class Quiz(models.Model):  
  title = models.CharField(max_length=100)  
  description = models.TextField()  
  video_url = models.CharField(max_length=255)  
  video_id = models.CharField(max_length=50, null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)  
  updated_at = models.DateTimeField(auto_now_add=True)  

  def __str__(self):
        return self.title

class QuizQuestion(models.Model):  
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')  
  question_title = models.CharField(max_length=255)  
  answer = models.CharField(max_length=255)  

  created_at = models.DateTimeField(auto_now_add=True)  
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.question_title

class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='question_options')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text