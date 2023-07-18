"""
Script to populate db with 50 tags and 25 todos
"""

import os
import random
import sys

import django
from faker import Faker

DJANGO_PROJECT_PATH = os.path.join(os.path.dirname(__file__), 'core')

sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

django.setup()

from todo.models import Tag, Todo

fake = Faker()

status = ['OPEN', 'WORKING', 'DONE', "OVERDUE"]
des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dignissimos, amet quod dolore debitis inventore sequi aliquam. Beatae in, nulla animi praesentium dolorem saepe molestiae ducimus amet vitae aliquam iste ipsa maiores nesciunt eum " \
      "voluptatum qui quibusdam illum eaque nostrum similique eligendi nisi. Itaque vero neque nihil, nostrum maiores laboriosam molestiae?"

for i in range(1, 51):
    Tag.objects.create(name=f"tag {i}")

tags = list(Tag.objects.all())

for i in range(1, 25):
    todo_tags = random.choices(tags, k=random.choice([1, 51]))
    my_todo = Todo.objects.create(title=f'todo {i}', due_date=fake.date_between(start_date='today', end_date='+30d'), status=random.choice(status), description=des, high_priority=random.getrandbits(1))
    my_todo.tags.set(todo_tags)
