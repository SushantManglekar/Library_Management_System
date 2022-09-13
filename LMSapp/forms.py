from django import forms  
from .models import Book  

# Create Form ManageForm
class ManageForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = "__all__"  