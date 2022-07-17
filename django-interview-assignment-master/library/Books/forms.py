from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'