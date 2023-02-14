from django.urls import path

from . import views

urlpatterns = [
    path('courses/add', views.add_course, name='add_course'),
    path('users', views.show_users, name='show_users'),
    path('', views.home, name='home'),
    path('add_student', views.add_student, name='add_student'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('register', views.register, name='register'),
    path('courses', views.show_courses, name='courses'),
    path('course/<course_id>', views.show_course, name='course'),
]
