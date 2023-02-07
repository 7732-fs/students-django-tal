from django.shortcuts import render
from django.contrib import messages
from .models import Course, User, Student
# Create your views here.

def add_course(request):
    if request.method=='POST':
        name=request.POST["course_name"]
        description=request.POST["description"]
        course=Course(name=name, description=description)
        course.save()
        request.session["user"]="anonymous"
    return render(request, "add_course.html", {"user":request.session.get("user", "not logged in")})

def add_student(request):
    if request.method=='POST':
        name=request.POST["student_name"]
        email=request.POST["student_email"]
        grade=request.POST["student_grade"]
        student=Student(name=name, email=email, grade=grade)
        student.save()
    return render(request)

def show_users(request):
    users=User.objects.all()
    return render(request, "users.html", {"users":users})