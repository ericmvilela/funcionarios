from django.contrib import admin
from .models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Funcionario, FuncionarioAdmin)
