from django.db import models

# Question Model
class Question(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Answer Model
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)