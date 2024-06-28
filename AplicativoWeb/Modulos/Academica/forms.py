# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed']
