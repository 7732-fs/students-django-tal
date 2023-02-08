from django.shortcuts import render, redirect, HttpResponse
from students2.models import Course, Student
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
# Create your views here.

def my_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("unauthorized")
    return render(request, 'login.html')

def home(request):
    return HttpResponse(f"hi {request.user} login at <a href='/login'>here</a>")

@login_required
def add_course(request):
    if request.method=='POST':
        name=request.POST["course_name"]
        description=request.POST["description"]
        course=Course(name=name, description=description)
        course.save()
    return render(request, "add_course.html", {"user":request.user })

def show_users(request):
    users=User.objects.all()
    return render(request, "users.html", {"users":users})

def register(request):
    student_name, student_email, student_course=request.GET.values()
    student=Student.objects.create(name=student_name, email=student_email)
    print(student_course)
    course=Course.objects.get(name=student_course)
    course.students.add(student)
    return HttpResponse(student.id)
