from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class TipoForm(forms.Form):
    tipos = (
        (1, 'Arrendatario'),
        (2, 'Arrendador'),
    )
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='RUT', max_length=12)
