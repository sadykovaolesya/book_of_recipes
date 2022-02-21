from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Author, RecipeIngredient, Recipe


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               }
    ))

    class Meta:
        model = Author
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ('username', 'email', 'password1',)


class IngredientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',)


IngredientFormset = forms.modelformset_factory(RecipeIngredient, form=IngredientForm, extra=1)


class AddRecipe(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Recipe
        exclude = ('author',)