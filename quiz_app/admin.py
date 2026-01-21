from django.contrib import admin
from .models import Quiz, QuizQuestion, QuizOption

admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizOption)