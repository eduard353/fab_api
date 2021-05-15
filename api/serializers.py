from rest_framework import serializers
from .models import Survey, Answers, Question, UserChoice


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'finish_date',)
        read_only_fields = ('start_date', )

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'question', 'answer',)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'question_type', 'survey',)

class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = ('id', 'user', 'survey', 'answer',)


