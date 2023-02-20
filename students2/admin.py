from django.contrib import admin
from .models import Student, Course
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Permission)

