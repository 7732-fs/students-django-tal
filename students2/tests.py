# from django.test import TestCase
import unittest
# from unittest import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from students2.models import Student
import os

client = Client()

# Create your tests here.


class StudentViewsTests(unittest.TestCase):
    def test_registration(self):
        response = client.get('/register?student_name=test&student_email=email&student_course=python')
        s = Student.objects.all().last()
        self.assertEqual(s.name, "test")
        self.assertIn("python", [c.name for c in s.course_set.all()])
