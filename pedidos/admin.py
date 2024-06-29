from django.contrib import admin
from .models import Pedido  # Importa el modelo Pedido desde models.py

# Registra el modelo Pedido en el panel de administración
admin.site.register(Pedido)