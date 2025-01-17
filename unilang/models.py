from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


