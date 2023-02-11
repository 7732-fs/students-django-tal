from django.shortcuts import render
from django.db.utils import IntegrityError
from .models import Course, User, Student, Teacher
from django.contrib import messages


# Create your views here.


def home(request, methods=["POST ,GET"]):
    return render(request, "home.html")


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

######
