import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "students2.settings")
from models import Student
import faker

fake=faker.Faker()
students=[ Student(name=fake.user_name(), email=fake.email()).save() for i in range(20)]