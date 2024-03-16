from django import forms

from .models import Post
""" from .models import ShoppingList
from .models import ShoppingListItem
from .models import ShoppingListQuantity """

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

""" class ShoppingListItemForm(forms.ModelForm):

    class Meta:
        model = ShoppingListItem
        fields = ('name', 'price')

class ShoppingLisrForm(forms.ModelForm):

    class Meta: 
        model = ShoppingList
        fields = ('name') """

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']