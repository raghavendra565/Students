from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    marks = models.IntegerField()
    def __str__(self):
        return self.name
class Subjects(models.Model):
    subject = models.CharField(max_length=20)
    faculty = models.CharField(max_length=20)
    def __str__(self):
        return self.faculty
