from django.db import models

class Course (models.Model):
    title = models.CharField(max_length=100)
    discribtion = models.TextField()
    duration = models.IntegerField

    def __str__(self):
        return self.title