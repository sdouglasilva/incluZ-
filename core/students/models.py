from django.db import models

class Student(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        date_of_birth = models.DateField()
        email = models.EmailField(unique=True)
        enrollment_date = models.DateField(auto_now_add=True)


        def __str__(self):
                return f"{self.first_name}{self.last_name} - {self.enrollment_date}"
