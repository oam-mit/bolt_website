from django import forms
from users.models import Profile
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    api_key=forms.CharField(widget=forms.TextInput(attrs={'class':'col-md-5','placeholder':'API Key of your Bolt Device',
        'type':'password'}),required=False, 
        help_text="<ul><li>Do not share your API Pin with anyone</li></ul>")
    device_name=forms.CharField(widget=forms.TextInput(attrs={'class':'col-md-5','placeholder':'Name of your Bolt Device'}),required=False)
    class Meta:
        model=Profile
        fields=['image','api_key','device_name']

class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'col-md-3'}),required=False)
    class Meta:
        model=User
        fields=['username']


