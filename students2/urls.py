from django.urls import path

from . import views

urlpatterns=[
    path('courses/add', views.add_course, name='add_course'),
    path('users', views.show_users, name='show_users'),
    path('', views.home, name='home'),
    path('/add_student',views.add_student,name='add_student')
]

# this is a comment
# this is Israel's comment
