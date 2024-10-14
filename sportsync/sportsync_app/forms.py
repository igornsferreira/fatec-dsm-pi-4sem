from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .models import Usuario


class CadastroForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        senha_confirm = cleaned_data.get('password_confirm')

        if senha != senha_confirm:
            raise forms.ValidationError('As senhas não coincidem.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.senha = make_password(self.cleaned_data["senha"])  # Criptografa a senha
        if commit:
            user.save()
        return user
    
class LoginEmailForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')
        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("Usuário não encontrado.")

        if not user.check_password(senha):
            raise forms.ValidationError("Senha incorreta.")
        return self.cleaned_data

