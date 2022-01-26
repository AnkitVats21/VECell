from django.db import models

# Create your models here.
class Certificate(models.Model):
    roll_no = models.CharField(max_length=55)
    student_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    total_attendance = models.IntegerField(default=0)
    reference_number = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.student_name}  {self.reference_number}'