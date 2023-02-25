from django.shortcuts import render, HttpResponse, redirect
from django.db.utils import IntegrityError
from .models import Course, User, Student, Teacher
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login, authenticate, logout
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required, permission_required
=======
from django.contrib.auth.decorators import login_required, permission_required 
from students2.forms import StudentForm
>>>>>>> 713cd7e7d4f60655f9e7987a623794771f63b547

# Create your views here.


def home(request, methods=["POST ,GET"]):
<<<<<<< HEAD
    if request.session
    logout_button = "logout"
    return render(request, "home.html", {"logout_button":logout_button})

=======
    if request.user.username!='':
        logout_button = "Log Out"
        link="/logout"
    else:
        logout_button = "Log In"
        link="/login"
    return render(request, "home.html", {"logout_button":logout_button, "link":link} )
>>>>>>> 713cd7e7d4f60655f9e7987a623794771f63b547

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

<<<<<<< HEAD

@login_required
@permission_required('students2.add_student')
=======
>>>>>>> 713cd7e7d4f60655f9e7987a623794771f63b547
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/students/admin/students")

def students(request):
    students=Student.objects.all()
    return render(request, "students.html", {"students":students})

def show_users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

def admin(request):
    return render(request, "admin.html")

def student_admin(request):
    form = StudentForm()
    return render(request, "students-admin.html", {"form":form})

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
