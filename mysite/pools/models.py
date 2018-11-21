from django.db import models


# Create your models here.

class Question(models.Model):
        question_text = models.CharField(max_length=180)
        pub_date = models.DateField()


class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete= models.CASCADE, related_name="quest")
        choice = models.CharField(max_length=180)
        vote = models.CharField(max_length=2)



