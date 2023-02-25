from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
<<<<<<< HEAD

    def __str__(self) -> str:
        return self.name
    
=======
    image=models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.name

>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4

class Course(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=512)
    students = models.ManyToManyField(Student)
    image=models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.name

<<<<<<< HEAD
=======
class Teacher(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    courses=models.ManyToManyField(Course)
    image=models.ImageField(upload_to='media/')
    description=models.TextField(max_length=1024)

    def __str__(self) -> str:
        return self.name


>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4

class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    role = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.username

<<<<<<< HEAD

class Teacher(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name
=======
class Message(models.Model):
    content=models.TextField(max_length=1024)
    source=models.ForeignKey(Student, verbose_name=("student_message"), on_delete=models.CASCADE)
    dest=models.ForeignKey(Teacher, verbose_name=("teacher_message"), on_delete=models.CASCADE)
>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4
