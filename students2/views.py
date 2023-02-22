from django.shortcuts import render, redirect, HttpResponse
from students2.models import Course, Student, Teacher
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from students2.forms import StudentForm, CourseForm, TeacherForm
from django.apps import apps

# Create your views here.

form_dict = {
    "students": StudentForm,
    "courses": CourseForm,
    "teachers": TeacherForm
}


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.path)
        else:
            raise PermissionDenied()
    return render(request, 'login.html')


def home(request):
    try:
        user = User.objects.get(username=request.user.username)
    except:
        user = "Anonymous User"
    return render(request, 'home.html', {user: user})


def logmeout(request):
    logout(request)
    return redirect('home')


@login_required
@permission_required('students2.view_student')
def show_users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


@login_required
@permission_required('students2.students_admin')
def admin(request, obj="students"):
    add_form = form_dict[obj]()
    return render(request, "admin.html", {"objects": apps.get_model(model_name=obj[:-1].capitalize(), app_label="students2").objects.all(), "obj_name": obj, "form": add_form})


def register(request):
    student_name, student_email, student_course = request.GET.values()
    student = Student.objects.create(name=student_name, email=student_email)
    course = Course.objects.get(name=student_course)
    course.students.add(student)
    return HttpResponse(student.id)


@login_required
@permission_required('students2.students_admin')
def update(request, obj, oid):
    model = apps.get_model(
        model_name=obj[:-1].capitalize(), app_label="students2").objects.get(pk=oid)
    form = form_dict[obj](instance=model)
    if request.method == 'POST':
        form = form_dict[obj](request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect(f"/students/admin/{obj}")
    else:
        return render(request, 'update.html', {"form": form})


@login_required
@permission_required('students2.students_admin')
def delete(request, obj, oid):
    apps.get_model(model_name=obj[:-1].capitalize(),
                   app_label="students2").objects.get(pk=oid).delete()
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


def search(request):
    q = request.GET.get("q", "")
    student_results = (Student.objects.filter(
        name__istartswith=q) | Student.objects.filter(email__istartswith=q)) or ["No results"]
    course_results = (Course.objects.filter(
        name__istartswith=q) | Course.objects.filter(description__icontains=q)) or ["No results"]
    teacher_results = (Teacher.objects.filter(
        name__startswith=q) | Teacher.objects.filter(email__startswith=q)) or ["No results"]
    return render(request, "search.html", {
        "students": student_results,
        "courses": course_results,
        "teachers": teacher_results
    })
