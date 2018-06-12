from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import Taskform

import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):

    username = factory.Sequence('testuser{}'.format)
    email = factory.Sequence(lambda a: 'testuser{0}@company.com'.format)
    password = "password"

    class Meta:
        model = User

# models test
class TaskTest(TestCase):

    def create_task(self, title="Title", description="A description"):
        user = UserFactory(username='bob')
        return Task.objects.create(title=title, pub_date=timezone.datetime.now(), completed=False, description=description, user=user)

    def test_task_creation(self):
        t = self.create_task()
        print(t.user.password)
        self.assertTrue(isinstance(t, Task))
        self.assertEqual(t.title, "Title")
        self.assertEqual(t.completed, False)
        self.assertEqual(t.description, "A description")
        self.assertEqual(t.user.username, 'bob')
