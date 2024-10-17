from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .models import Usuario

class CadastroForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('As senhas não coincidem.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class LoginEmailForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("Usuário não encontrado.")

        if not user.check_password(password):
            raise forms.ValidationError("Senha incorreta.") 
        return self.cleaned_data
