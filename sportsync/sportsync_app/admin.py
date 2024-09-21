from django.contrib import admin
from .models import Endereco, Usuario, Esporte, Evento, Partida, Quadra, UsuarioPartida, UsuarioEvento

admin.site.register(Endereco)
admin.site.register(Usuario)
admin.site.register(Esporte)
admin.site.register(Evento)
admin.site.register(Partida)
admin.site.register(Quadra)
admin.site.register(UsuarioPartida)
admin.site.register(UsuarioEvento)
