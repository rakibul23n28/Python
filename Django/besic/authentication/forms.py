from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
    def label_tag(self, contents=None, attrs=None, label_suffix=None):
        if attrs is None:
            attrs = {}
        attrs.setdefault('class', 'form-label ')  # Add Bootstrap class to label
        return super().label_tag(contents=contents, attrs=attrs, label_suffix=label_suffix)