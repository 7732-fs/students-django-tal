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


def home(request, methods=["POST ,GET"]):
    if request.session:
    logout_button = "logout"
    return render(request, "home.html", {"logout_button": logout_button})

    if request.user.username!='':
        log='Log Out'
        log_link='/logout'
    else:
        log='Log In'
        log_link='/login'
    return render(request, "home.html", {'log':log, 'log_link':log_link})

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
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/students/admin/students")


def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == "admin":
                return redirect('students_admin')
            app_user = Student.objects.get(name=user.email)
            return redirect(f"/student/{app_user.id}")
        else:
            raise PermissionDenied()
    request.session['next'] = request.GET.get("next", "/")
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

def admin(request):
    return render(request,"admin.html")


@login_required
def student(request, sid=0):
    students = Student.objects.all()
    student = Student.objects.filter(pk=sid).first()
    return render(request, "student.html", {"student": student, "students": students})


def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def course(request, cid=0):
    courses = Course.objects.all()
    course = Course.objects.get(pk=cid)
    return render(request, "course.html", {"course": course, "courses": courses})


@login_required
def teacher(request, tid=0):
    teachers = Teacher.objects.all()
    student = Teacher.objects.filter(pk=tid).first() or User.objects.get(username="admin")
    return render(request, "teacher.html", {"teacher": teacher, "teachers": teachers})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})


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
        form = form_dict[obj](request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
            return redirect(f"/students/admin/{obj}")
    else:
        return render(request, 'update.html', {"form": form, "obj_name": obj, "oid": oid})


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
        form = StudentForm(request.POST, request.FILES)
    if obj == "courses":
        form = CourseForm(request.POST, request.FILES)
    if obj == "teachers":
        form = TeacherForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            if obj == "students":
                User.objects.create_user(email=form.cleaned_data["email"], username=form.cleaned_data["email"], password="1234")
            form.save()
            return redirect(f"/students/admin/{obj}")
        else:
            print(form.errors)
    else:
        return render(request, 'add.html', {"form": form})


def search(request):
    q = request.GET.get("q", "")
    student_results = (Student.objects.filter(
        name__istartswith=q) | Student.objects.filter(email__istartswith=q))
    course_results = (Course.objects.filter(
        name__istartswith=q) | Course.objects.filter(description__icontains=q))
    teacher_results = (Teacher.objects.filter(
        name__startswith=q) | Teacher.objects.filter(email__startswith=q))
    return render(request, "search.html", {
        "students": student_results,
        "courses": course_results,
        "teachers": teacher_results
    })
