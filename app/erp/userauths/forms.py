from django import forms
from django.contrib.auth.forms import UserCreationForm
from erp.userauths.models import User, Profile


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


    class Meta:
        model = User
        fields = ['username','email']


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-3'


    nombres = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombres '}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellidos '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    cod_contri_rentas = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Introduzca su Codigo de rentas ', 'type':'number'}))
    cod_predial_rentas = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Introduzca su Codigo Predial de rentas ', 'type':'number'}))
    cod_predial_rentas = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Introduzca su Codigo Predial de rentas ', 'type':'number'}))
    DNI = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Introduzca su DNI', 'type':'number'}))

    class Meta:
        model = Profile
        fields = ['nombres', 'DNI','image', 'telefono', 'email', 'apellidos','cod_contri_rentas','cod_predial_rentas','ruc','persona_juridica']  # Incluye el campo email en la lista de campos
        exclude = ['Deudas',]


