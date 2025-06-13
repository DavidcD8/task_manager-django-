from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # This enables a drop-down calendar
        }

class TaskSearchForm(forms.Form):
    q = forms.CharField(required=False, label="Search")
    completed = forms.ChoiceField(
        required=False,
        choices=[('', 'All'), ('1', 'Completed'), ('0', 'Not Completed')],
        label="Status"
    )