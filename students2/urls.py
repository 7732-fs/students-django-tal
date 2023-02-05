from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.my_login, name='my_login'),
    path('admin/', admin.site.urls),
    path('courses/add', views.add_course, name='add_course'),
    path('users', views.show_users, name='show_users')
]