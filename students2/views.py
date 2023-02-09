from django.shortcuts import render
from .models import Course, User
from django.db.utils import IntegrityError
# Create your views here.

def add_course(request):
    message = ""
    try:
        if request.method=='POST':
            name=request.POST["course_name"]
            description=request.POST["description"]
            course=Course(name=name, description=description)
            course.save()
            request.session["user"]="anonymous"
            message = f"{name} Added successfully"
        return render(request, "add_course.html",  {"user":request.session.get("user", "not logged in"), "message":message})
    except IntegrityError:
        message = (f"{name} Already exists")
        return render(request, "add_course.html", {"user":request.session.get("user", "not logged in"), "message":message})

def show_users(request):
    users=User.objects.all()
    return render(request, "users.html", {"users":users})