from django import forms
from ActivityPeriod.models import User

class UserList(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']
    