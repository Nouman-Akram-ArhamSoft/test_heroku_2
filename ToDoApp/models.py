from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.


class Person(User):


    user_DOB = models.DateField(blank=False)
    REQUIRED_FIELDS = ['username', 'email', 'password']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    task_title = models.CharField(max_length=200, blank=False)
    task_description = models.TextField(blank=True)
    is_complete = models.BooleanField(blank=False, default=False)

    # Category variables
    HT = 'Home Task'
    OT = 'Office Task'
    MISC = 'Miscellenious Task'

    category = [
        (HT , "Home Task"),
        (OT, "Office Task"),
        (MISC, 'Mescillineous')
    ]

    task_category = models.CharField(max_length=20, choices=category, blank=False)
    task_start_date = models.DateTimeField(default=datetime.now())
    task_end_date = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.task_title

