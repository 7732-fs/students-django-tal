from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.my_login, name='my_login'),
    path('admin/', admin.site.urls),
    path('users', views.show_users, name='show_users'),    
    path('register', views.register, name='register'),
    path('students/admin', views.admin, name='students_admin'),
    path('<obj>/add/', views.add, name='object_add'),
    path('<obj>/update/<oid>', views.update, name='object_update'),
    path('<obj>/delete/<oid>', views.delete, name='object_delete'),
    path('students/admin/<obj>', views.admin, name='admin_object')
]