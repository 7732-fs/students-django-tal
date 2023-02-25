from django.contrib import admin
<<<<<<< HEAD
from .models import Student, Course, Teacher
=======
from .models import Student, Course
from django.contrib.auth.models import Permission
>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
<<<<<<< HEAD
admin.site.register(Teacher)
=======
admin.site.register(Permission)

>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4
