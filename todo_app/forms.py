from django import forms
from . import models
class TaskForm(forms.ModelForm):
    work = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter a new task','class':'work'}))
    class Meta:    
        model = models.Task
        fields = '__all__'