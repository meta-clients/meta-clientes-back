from django.contrib import admin
from .models import ClientModel, ChildrenModel

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone","has_child","number_of_children", "created_at","updated_at"]


@admin.register(ChildrenModel)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ["gender","clother_size","client", "created_at","updated_at"]
    