from django.contrib import admin
from .models import Quiz, QuizQuestion, QuizOption

class QuizExtension(admin.ModelAdmin):
    list_filter= ['id','title', 'video_url', 'video_id', 'created_at', 'updated_at']
    list_display = ('id','title', 'video_url', 'video_id')
    readonly_fields = ['id']

class QuizQuestionExtension(admin.ModelAdmin):
    list_filter= ['id','quiz','question_title','created_at', 'updated_at']
    list_display = ('id','quiz','question_title', 'answer')
    readonly_fields = ['id','quiz']

class QuizOptionExtension(admin.ModelAdmin):
    list_filter= ['id','question','text']
    list_display = ('id','question','text')
    readonly_fields = ['id','question']

admin.site.register(Quiz, QuizExtension)
admin.site.register(QuizQuestion, QuizQuestionExtension)
admin.site.register(QuizOption, QuizOptionExtension)