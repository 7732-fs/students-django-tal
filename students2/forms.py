from django import forms
from students2.models import Student, Course, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
<<<<<<< HEAD
=======
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4
        fields = '__all__'