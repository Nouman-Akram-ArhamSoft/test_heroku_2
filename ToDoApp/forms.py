from .models import Person, Task
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms.widgets import DateInput, PasswordInput
# Create your views here.
class RegistrationForm(UserCreationForm):

    class Meta:
        model = Person

        labels = {
            'user_DOB': ('D.O.B'),
        }
        widgets = {
            'user_DOB': DateInput(attrs={'type': 'date'})
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'user_DOB']

        exclude = ['last_login', 'is_superuser', 'is_active', 'groups', 'user_permissions', 'date_joined', 'is_staff']


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = '__all__'

        exclude = ['is_complete', 'task_start_date', 'task_end_date', 'person']
        # ['task_title', 'task_description', 'is_complete',
        #                   'task_category', 'task_start_date', 'task_end_date','person']




