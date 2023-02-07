from django.shortcuts import render
from .models import Course, User, Student
<<<<<<< HEAD
from django.contrib import messages
=======
>>>>>>> bc5b6ce192b72a2ecd1534cf049e4f39988464b9
# Create your views here.

def home(request,methods=["POST ,GET"]):
    return render(request,"home.html")

def add_course(request):
    if request.method=='POST':
        name=request.POST["course_name"]
        description=request.POST["description"]
        course=Course(name=name, description=description)
        course.save()
        request.session["user"]="anonymous"
        if "user" in request.session:
            return render(request, "add_course.html", {"user":f'You are logged in as {request.session.get("user")}'})
        else:
            return render(request, "add_course.html", {"user":"You are not logged in"})
    else:
        return render(request, "add_course.html", {"user":"You are not logged in"})

def add_student(request):
    if request.method=='POST':
        name=request.POST["student_name"]
        email=request.POST["student_email"]
        grade=request.POST["student_grade"]
        student=Student(name=name, email=email, grade=grade)
        student.save()
    return render(request, "add_student.html")

def show_users(request):
    users=User.objects.all()
    return render(request, "users.html", {"users":users})




