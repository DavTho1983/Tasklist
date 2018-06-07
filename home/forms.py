from django import forms
from .models import Task

from django.utils import timezone

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
