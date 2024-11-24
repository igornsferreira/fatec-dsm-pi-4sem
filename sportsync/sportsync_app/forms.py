from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from .models import Usuario


class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha', max_length=128)
    confirmacao_senha = forms.CharField(widget=forms.PasswordInput, label='Confirme sua senha', max_length=128)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'senha']
        widgets = {
            'senha': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
            'confirmacao_senha': forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise ValidationError(_('O nome é obrigatório.'))
        return nome

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError(_('O email é obrigatório.'))
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError(_('Este email já está em uso.'))
        return email

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone:
            raise ValidationError(_('O telefone é obrigatório.'))
        return telefone

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        if not senha:
            raise ValidationError(_('A senha é obrigatória.'))
        if len(senha) < 8:
            raise ValidationError(_('A senha deve ter pelo menos 8 caracteres.'))
        if not re.search(r'[A-Z]', senha):
            raise ValidationError(_('A senha deve conter pelo menos uma letra maiúscula.'))
        if not re.search(r'[0-9]', senha):
            raise ValidationError(_('A senha deve conter pelo menos um número.'))
        if not re.search(r'[\W_]', senha):
            raise ValidationError(_('A senha deve conter pelo menos um caractere especial.'))
        return senha

    def clean_confirmacao_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmacao_senha = self.cleaned_data.get('confirmacao_senha')

        if senha and confirmacao_senha and senha != confirmacao_senha:
            raise ValidationError(_('As senhas não correspondem.'))
        return confirmacao_senha

    def save(self, commit=True):
        usuario = super().save(commit=False)  
        usuario.set_password(self.cleaned_data['senha'])  
        if commit:
            usuario.save()
        return usuario

class LoginEmailForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError(_('O email é obrigatório.'))
        return email

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        if not senha:
            raise ValidationError(_('A senha é obrigatória.'))
        return senha