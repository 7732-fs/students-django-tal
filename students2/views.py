from django.shortcuts import render, redirect, HttpResponse
from students2.models import Course, Student, Teacher
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from students2.forms import StudentForm, CourseForm, TeacherForm
from django.apps import apps

# Create your views here.

def my_login(request):
    if request.method == 'POST':
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
    user = User.objects.get(username=request.user.username)
    return render(request, 'home.html', {user: user})



@login_required
@permission_required('students2.view_student')
def show_users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


@login_required
@permission_required('students2.students_admin')
def admin(request, obj="students"):
    return render(request, "admin.html", {"objects": apps.get_model(model_name=obj[:-1].capitalize(), app_label="students2").objects.all(), "obj_name": obj})


def register(request):
    student_name, student_email, student_course = request.GET.values()
    student = Student.objects.create(name=student_name, email=student_email)
    course = Course.objects.get(name=student_course)
    course.students.add(student)
    return HttpResponse(student.id)

form_dict={
    "students":StudentForm,
    "courses":CourseForm,
    "teachers":TeacherForm
}

@login_required
@permission_required('students2.students_admin')
def update(request, obj, oid):
    model=apps.get_model(model_name=obj[:-1].capitalize(), app_label="students2").objects.get(pk=oid)
    form=form_dict[obj](instance=model)
    if request.method == 'POST':
        form=form_dict[obj](request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect(f"/students/admin/{obj}")
    else:
        return render(request, 'update.html', {"form": form})


@login_required
@permission_required('students2.students_admin')
def delete(request, obj, oid):
    apps.get_model(model_name=obj[:-1].capitalize(), app_label="students2").objects.get(pk=oid).delete()
    return redirect(f"/students/admin/{obj}")


@login_required
@permission_required('students2.students_admin')
def add(request, obj):
    if obj == "students":
        form = StudentForm(request.POST)
    if obj == "courses":
        form = CourseForm(request.POST)
    if obj == "teachers":
        form = TeacherForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(f"/students/admin/{obj}")
    else:
        return render(request, 'add.html', {"form": form})

