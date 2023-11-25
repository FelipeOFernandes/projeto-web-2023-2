from django.contrib import admin
from .models import Produto, Prato, PratoProduto

admin.site.register(Produto)
admin.site.register(Prato)
admin.site.register(PratoProduto)

# Register your models here.
