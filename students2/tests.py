from django.test import TestCase, Client
from students2.models import Student

# Create your tests here.

client=Client()

class StudentRegisterTest(TestCase):
    def test_register(self):
        client.get("http://127.0.0.1:8000/register?name=test&email=test@test.com&grade=99")
        student=Student.objects.all().last()
        self.assertEqual(student.name, "test")
        
