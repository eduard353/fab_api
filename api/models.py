from django.db import models
from datetime import date


# Create your models here.

class Survey(models.Model):
    """Класс описывающий модель опросов"""

    name = models.CharField(max_length=200, null=False)
    start_date = models.DateField(default=date.today())
    finish_date = models.DateField()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'опросы'
        ordering = ['start_date']

    def __str__(self):
        return self.name


class Question(models.Model):
    """Класс описывающий можель вопросов"""

    question_type_choice = (
        ('Ответ текстом', 'txt'),
        ('Ответ с выбором одного варианта', 'sng'),
        ('Ответ с выбором нескольких вариантов', 'mlt')
    )
    text = models.TextField(max_length=500, null=False)
    question_type = models.CharField(max_length=50, default='Ответ текстом', choices=question_type_choice,
                                     verbose_name='тип вопроса')
    survey = models.ForeignKey(Survey, related_name='question', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['survey']

    def __str__(self):
        return self.text


class Answers(models.Model):
    """Класс описывающий модель ответов на вопросы"""

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['question']

    def __str__(self):
        return self.answer


class UserChoice(models.Model):
    """Класс описывающий модель ответов пользователя на вопросы опроса"""
    user = models.IntegerField()
    survey = models.ForeignKey(Survey, related_name='user', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE, default=1)
    answer = models.ForeignKey(Answers, related_name='user_answer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Выбор пользователя'
        verbose_name_plural = 'выбор пользователя'
        ordering = ['user']

    def __str__(self):
        return str(self.user) + ' - ' + str(self.question.text) + ' - ' + str(self.answer.answer)
