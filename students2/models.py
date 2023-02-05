from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    grade = models.IntegerField(default=0)

class Course(models.Model):
    name=models.CharField(max_length=256, unique=True)
    description=models.CharField(max_length=512)
    students = models.ManyToManyField(Student)

    def __str__(self) -> str:
        return self.name

class User(models.Model):
    username=models.CharField(max_length=256)
    password=models.CharField(max_length=256)
    role=models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.username
