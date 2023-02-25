<<<<<<< HEAD
from django.test import TestCase, Client
from students2.models import Student

# Create your tests here.

client=Client()

class StudentRegisterTest(TestCase):
    def test_register(self):
        client.get("http://127.0.0.1:8000/register?name=test&email=test@test.com&grade=99")
        student=Student.objects.all().last()
        self.assertEqual(student.name, "test")
        
=======
#from django.test import TestCase
import unittest
#from unittest import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from students2.models import Student
import os

client = Client()

# Create your tests here.

class StudentViewsTests(unittest.TestCase):
    def test_registration(self):    
        response = client.get('/register?student_name=test&student_email=email&student_course=python')
        s=Student.objects.all().last()
        self.assertEqual(s.name, "test")
        self.assertIn("python", [ c.name for c in s.course_set.all() ])

>>>>>>> f41926ab0dd739b3ce000e473356591a1a6037e4
