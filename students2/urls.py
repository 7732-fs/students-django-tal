from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    path('admin', admin.site.urls),
    path('add_course', views.add_course, name='add_course'),
    path('login', views.app_login, name='login'),
    path('logout', views.app_logout, name='logout'),
    path('users', views.show_users, name='show_users'),
    path('', views.home, name='home'),
    path('students', views.students, name='students'),
    path('students/admin', views.admin, name='students_admin'),
    path('students/admin/students', views.student_admin, name='student_admin'),
    path('students/admin/courses', views.course_admin, name='course_admin'),
    path('students/admin/teachers', views.admin, name='admin'),
    path('add_student', views.add_student, name='add_student'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('register', views.register, name='register'),
    path('courses', views.show_courses, name='courses'),
    path('course/<course_id>', views.show_course, name='course'),
    path('course/<course_id>/<student_id>', views.add_student_to_course, name='add_student_course'),

]
