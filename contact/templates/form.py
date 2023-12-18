from django import forms
from ..models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ('name', 'email', 'telephone', 'message')
        fields = '__all__'