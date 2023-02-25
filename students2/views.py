from django.shortcuts import render, HttpResponse, redirect
from django.db.utils import IntegrityError
from .models import Course, User, Student, Teacher
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def home(request, methods=["POST ,GET"]):
    if request.session
    logout_button = "logout"
    return render(request, "home.html", {"logout_button":logout_button})


def app_login(request):
    if request.method == 'POST':
        (username, password) = (request.POST['username'], request.POST['password'])
        user = authenticate(request, username=username, password=password)
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
    message = ""
    try:
        if request.method == 'POST':
            name = request.POST["course_name"]
            description = request.POST["description"]
            course = Course(name=name, description=description)
            course.save()
            request.session["user"] = "anonymous"
            message = f"{name} Added successfully"
            if "user" in request.session:
                return render(request, "add_course.html", {"user": f'You are logged in as {request.session.get("user")}', "message": message})
            else:
                return render(request, "add_course.html", {"user": "You are not logged in",  "message": message})
        else:
            return render(request, "add_course.html", {"user": "You are not logged in",  "message": message})

    except IntegrityError:
        message = (f"{name} Already exists")
        return render(request, "add_course.html", {"user": request.session.get("user", "not logged in"), "message": message})


@login_required
@permission_required('students2.add_student')
def add_student(request):
    msg = ""
    if request.method == 'POST':
        name = request.POST["student_name"]
        email = request.POST["student_email"]
        grade = request.POST["student_grade"]
        student = Student(name=name, email=email, grade=grade)
        student.save()
        msg = messages.success(request, f"{student.name} Added to DB")
    return render(request, "add_student.html", {"message": msg})


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
    student = Student.objects.create(**dict(request.GET.items()))
    Course.objects.get(name="python").students.add(student)
    return HttpResponse(student.name)


def show_courses(request):
    return render(request, "courses.html", {"courses": Course.objects.all()})


def show_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    students = Student.objects.all()
    registered = course.students.all()
    return render(request, "course.html", {"course": course, "students": students, "registered": registered})


def add_student_to_course(request, student_id, course_id):
    course = Course.objects.get(id=course_id)
    student = Student.objects.get(id=student_id)
    course.students.add(student)
    return redirect(f"/course/{course_id}")
