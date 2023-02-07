from django.urls import path

from . import views

urlpatterns=[
    path('courses/add', views.add_course, name='add_course'),
    path('users', views.show_users, name='show_users'),
    path('', views.home, name='home')
]

# this is a comment