from django.db import models


class Question1(models.Model):
    question_text1 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice1(models.Model):
    question = models.ForeignKey(Question1, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
