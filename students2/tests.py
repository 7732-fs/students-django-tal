from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from students2.models import Student

client = Client()

# Create your tests here.

class StudentViewsTests(TestCase):
    def test_registration(self):    
        response = client.get('/register?student_name=test&student_email=email&student_course=python')
        s=Student.objects.all().last()
        self.assertEqual(s.name, "test")
        self.assertContains(s.course_set(), "test")
