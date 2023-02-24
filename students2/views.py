from django.shortcuts import render, HttpResponse, redirect
from django.db.utils import IntegrityError

from students2.forms import CourseForm, StudentForm
from .models import Course, User, Student, Teacher
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required 

# Create your views here.

def home(request, methods=["POST ,GET"]):
    if request.user.username != '':
        log_button = "Log Out"
        link = "/logout"
    else:
        log_button = "Log In"
        link = "/login"
    return render(request, "home.html",{"log_button":log_button,"log_link":link})

def admin(request):
    return render(request,"admin.html")

def student_admin(request):
    form = StudentForm
    return render(request,"students_admin.html", {"form":form})

def course_admin(request):
    form = CourseForm
    return render(request,"courses_admin.html", {"form":form})


def app_login(request):
    if request.method=='POST':
        (username, password)=(request.POST['username'], request.POST['password'])
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("wrong login or password")
    return render(request, "login.html")

def app_logout(request):
    logout(request)
    return redirect('home')

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/students/admin/courses")

@login_required
@permission_required('students2.add_student')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # email = form.cleaned_data["email"]
            # name = form.cleaned_data["name"]
            # student = Student(name=name, email=email,)
            form.save()
        return redirect("/students/admin/students")

def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students":students})
def show_users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


def add_teacher(request):
    message = ""
    try:
        if request.method == 'POST':
            name = request.POST["name"]
            email = request.POST["email"]
            teacher = Teacher(name=name, email=email)
            teacher.save()
            message = f"{name} Added successfully"
            if "user" in request.session:
                return render(request, "add_teacher.html", {"user": f'You are logged in as {request.session.get("user")}', "message": message})
            else:
                return render(request, "add_teacher.html", {"user": "You are not logged in",  "message": message})
        else:
            return render(request, "add_teacher.html", {"user": "You are not logged in",  "message": message})
    except IntegrityError:
        message = (f"{name} Already exists")
        if "user" in request.session:
            return render(request, "add_teacher.html", {"user": f'You are logged in as {request.session.get("user")}', "message": message})
        else:
            return render(request, "add_teacher.html", {"user": "You are not logged in",  "message": message})

def register(request):
    student=Student.objects.create(**dict(request.GET.items()))
    Course.objects.get(name="python").students.add(student)
    return HttpResponse(student.name)

def show_courses(request):
    return render(request, "courses.html", {"courses":Course.objects.all()})

def show_course(request, course_id):
    course=Course.objects.get(pk=course_id)
    students=Student.objects.all()
    registered=course.students.all()
    return render(request, "course.html", {"course":course, "students":students, "registered":registered})

def add_student_to_course(request, student_id, course_id):
    course=Course.objects.get(id=course_id)
    student=Student.objects.get(id=student_id)
    course.students.add(student)
    return redirect(f"/course/{course_id}")
    
