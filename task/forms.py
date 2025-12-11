from django import forms

from task.models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple
        }