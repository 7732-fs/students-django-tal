from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('courses/add', views.add_course, name='add_course'),
    path('login', views.app_login, name='login'),
    path('logout', views.app_logout, name='logout'),
    path('students', views.students, name='students'),
    path('students/admin', views.admin, name='app_admin'),
    path('students/admin/students', views.student_admin, name='students_admin'),
    path('students/admin/courses', views.admin, name='students_admin'),
    path('students/admin/teachers', views.admin, name='students_admin'),
    path('users', views.show_users, name='show_users'),
    path('', views.home, name='home'),
    path('add_student', views.add_student, name='add_student'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('register', views.register, name='register'),
    path('courses', views.show_courses, name='courses'),
    path('course/<course_id>', views.show_course, name='course'),
    path('course/<course_id>/<student_id>', views.add_student_to_course, name='add_student_course'),

]
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
