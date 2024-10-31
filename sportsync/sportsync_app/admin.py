from django.contrib import admin
from .models import Usuario, Esporte, Endereco, Quadra, Partida, UsuarioPartida

# Registro dos modelos no Django Admin
admin.site.register(Usuario)
admin.site.register(Esporte)
admin.site.register(Endereco)
admin.site.register(Quadra)
admin.site.register(Partida)
admin.site.register(UsuarioPartida)
