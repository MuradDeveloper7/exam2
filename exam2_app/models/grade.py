from django.db import models

class Grade(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateField()
    course = models.ForeignKey("exam2_app.Course", on_delete=models.CASCADE)
    student = models.ForeignKey("exam2_app.Student", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.course}: {self.value}"