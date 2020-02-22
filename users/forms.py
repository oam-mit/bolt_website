from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'abc_123'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'abc@abc.com'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'ABC'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'XYZ'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'XXXXXXXXXX'}),
        help_text='<ol><li>Passwords are not stored in Raw Form. Hence even the admins cannot see your Password</li><li>Password cannot be very similar to your username</li></ol>',
        label='Enter Password')

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter the above Password'}),
    label='Re-enter your Password')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    
    def save(self,commit=True):
        user=super(UserRegisterForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['username']
        if commit:
            user.save()
        
        return user


class FeedbackForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'XYZ'}))
    surname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ABC'}))
    
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'abc_123'}),
    required=False,
    help_text='<ul><li>If you do not have a username yet, please leave this field blank</li></ul>')
    country=forms.ChoiceField(choices=Feedback.choices,widget=forms.Select(attrs={'class':'col-md-3'}))

    number=forms.CharField(min_length=10,max_length=15,widget=forms.TextInput(attrs={'placeholder':'1234567890','class':'col-md-3'}))

    feedback=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'placeholder':'Maximum of 1000 characters','onkeydown':'change()'}),help_text="Currently Typed: 0")
    class Meta:
        model=Feedback
        fields=['name','surname','username','country','number','feedback']

    

    def is_unique(self,name,surname,country,number):
        check1=1
        check2=1
        try:
            Feedback.objects.get(name=name,surname=surname)
            check1=0
        except:
            check1=1
        try:
            Feedback.objects.get(code=country,number=number)
            check2=0
        except:
            check2=1
        
        if check1==1 and check2==1:
            return True
        else:
            return False
    
    def check_user(self,username):
        check=0
        if not username:
            return True
        try:
           User.objects.get(username=username)
           check=1
        except:
            check=0
            
        if check==1:
            return True