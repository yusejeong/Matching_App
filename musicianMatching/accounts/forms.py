from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields=['username','first_name','last_name','email']

class CustomUserCreationForm(UserCreationForm):
    address = 
    class Meta:
        model=get_user_model()
        fields=['username','email','address']