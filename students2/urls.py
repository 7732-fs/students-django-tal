from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.my_login, name='my_login'),
    path('logout', views.logmeout, name='logout'),
    path('admin/', admin.site.urls),
    path('users', views.show_users, name='show_users'),    
    path('search', views.search, name='search'),    
    path('register', views.register, name='register'),
    path('students/admin', views.admin, name='students_admin'),
    path('students', views.student, name='students'),
    path('student/<sid>', views.student, name='student'),
    path('courses', views.courses, name='courses'),
    path('course/<cid>', views.course, name='course'),
    path('teachers', views.teachers, name='teachers'),
    path('teacher/<tid>', views.teacher, name='teacher'),
    path('<obj>/add/', views.add, name='object_add'),
    path('<obj>/update/<oid>', views.update, name='object_update'),
    path('<obj>/delete/<oid>', views.delete, name='object_delete'),
    path('students/admin/<obj>', views.admin, name='admin_object')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)