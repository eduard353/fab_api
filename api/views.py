from datetime import date
from .models import Survey, Answers, Question, UserChoice
from .serializers import SurveySerializer, AnswersSerializer, QuestionSerializer, UserChoiceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='get', operation_description="Просмотр активных опросов")
@api_view(['GET'])
def api_surveys(request):
    """Просмотр активных опросов"""
    if request.method == 'GET':
        act_surveys = Survey.objects.filter(finish_date__gt=date.today()).filter(start_date__lt=date.today())
        serializer = SurveySerializer(act_surveys, many=True)
        return Response(serializer.data)


@swagger_auto_schema(method='post', operation_description="Добавление нового опроса", request_body=SurveySerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_surveys_create(request):
    if request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(method='get', operation_description="Просмотр детальной информации по опросу")
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_survey_detail(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    if request.method == 'GET':
        serializer = SurveySerializer(survey)
        return Response(serializer.data)


@swagger_auto_schema(methods=['put', 'patch'], operation_description="Изменение опроса", request_body=SurveySerializer)
@swagger_auto_schema(method='delete', operation_description="Удаление опроса")
@api_view(['PUT', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_survey_modify(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', operation_description="Просмотр всех вопросов")
@api_view(['GET', ])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_questions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


@swagger_auto_schema(method='post', operation_description="Добавление нового вопроса", request_body=QuestionSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_questions_create(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['put', 'patch'], operation_description="Изменение вопроса",
                     request_body=QuestionSerializer)
@swagger_auto_schema(method='delete', operation_description="Удаление вопроса")
@swagger_auto_schema(method='get', operation_description="Просмотр одного вопроса")
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', operation_description="Просмотр всех ответов")
@api_view(['GET', ])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_answers(request):
    if request.method == 'GET':
        answers = Answers.objects.all()
        serializer = QuestionSerializer(answers, many=True)
        return Response(serializer.data)


@swagger_auto_schema(method='post', operation_description="Добавление нового ответа", request_body=AnswersSerializer)
@api_view(['POST', ])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_answers_create(request):
    if request.method == 'POST':
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(methods=['put', 'patch'], operation_description="Изменение ответа",
                     request_body=AnswersSerializer)
@swagger_auto_schema(method='delete', operation_description="Удаление ответа")
@swagger_auto_schema(method='get', operation_description="Просмотр одного ответа")
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def api_answer_detail(request, answer_id):
    answer = Answers.objects.get(pk=answer_id)
    if request.method == 'GET':
        serializer = AnswersSerializer(answer)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = AnswersSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', operation_description="Просмотр ответов пользователя")
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_user_answers(request, user_id):
    if request.method == 'GET':
        user_answers = UserChoice.objects.filter(user=user_id)
        serializer = UserChoiceSerializer(user_answers, many=True)
        return Response(serializer.data)
