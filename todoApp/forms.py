from django import forms 
from .models import CreateTodo
 
    
class ToDoForm(forms.ModelForm):
    class Meta:
        model = CreateTodo
        fields = "__all__"
        
        