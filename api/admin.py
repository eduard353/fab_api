from django.contrib import admin
from .models import Survey, Answers, Question, UserChoice


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'finish_date',)

@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'correct',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type', 'survey',)

@admin.register(UserChoice)
class UserChoice(admin.ModelAdmin):
    list_display = ('user', 'survey', 'question', 'answer',)

# Register your models here.
