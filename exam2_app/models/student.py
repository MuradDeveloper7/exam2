from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField("exam2_app.Course", through='Enrollment')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"