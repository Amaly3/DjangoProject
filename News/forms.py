from django import forms
from django.contrib.auth.forms import UserCreationForm

from Home.models import MyUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    #phone_no = forms.CharField(max_length=100)
    #national_id=forms.CharField(max_length=2)regex=r'^\+?1?\d{9,15}$',
    national_id = forms.RegexField(regex=r'(2|1)\d{9}')#,error_message = ("Phone number must be entered in the format: '+966 or 00966 or 05 or 5'. Up to 10 digits is allowed."))
    phone_no = forms.RegexField(regex=r'(05|5)\d{8}')#,error_message = ("Phone number must be entered in the format: '+966 or 00966 or 05 or 5'. Up to 10 digits is allowed."))
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    class Meta:
        model = MyUser
        fields = ['username', 'email','date_of_birth','phone_no' ,'national_id','password1', 'password2']