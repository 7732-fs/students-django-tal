from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    image=models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=256, unique=True)
    description=models.CharField(max_length=512)
    students = models.ManyToManyField(Student)

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    courses=models.ManyToManyField(Course)


class User(models.Model):
    username=models.CharField(max_length=256)
    password=models.CharField(max_length=256)
    role=models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.username

class Message(models.Model):
    content=models.TextField(max_length=1024)
    source=models.ForeignKey(Student, verbose_name=("student_message"), on_delete=models.CASCADE)
    dest=models.ForeignKey(Teacher, verbose_name=("teacher_message"), on_delete=models.CASCADE)