from django.shortcuts import render, redirect, HttpResponse
from students2.models import Course, Student
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

 

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
            raise PermissionDenied()
    return render(request, 'login.html')

def home(request):
    user=User.objects.get(username=request.user.username)
    return render(request, 'home.html', {user:user})

@login_required
@permission_required('students2.add_student')
def add_course(request):
    if request.method=='POST':
        name=request.POST["course_name"]
        description=request.POST["description"]
        course=Course(name=name, description=description)
        course.save()
    return render(request, "add_course.html", {"user":request.user })

@login_required
@permission_required('students2.view_student')
def show_users(request):
    users=User.objects.all()
    return render(request, "users.html", {"users":users})

@login_required
@permission_required('students2.students_admin')
def admin(request, obj=""):
    if obj=="students":
        return render(request, "admin.html", {"objects":Student.objects.all()})
    return render(request, "admin.html", {"objects":obj})

def register(request):
    student_name, student_email, student_course=request.GET.values()
    student=Student.objects.create(name=student_name, email=student_email)
    course=Course.objects.get(name=student_course)
    course.students.add(student)
    return HttpResponse(student.id)

