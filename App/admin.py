from django.contrib import admin
from .models import Service, Contact, QueryType
# Register your models here.

#HomeAdmin del Servicio
class Homeadmin(admin.ModelAdmin):
    list_display =["id","name","price"]
    search_fields = ["name",]
    ordering = ('-id',)
    list_per_page = 10
    list_filter =["price"]

#HomeAdmin de las Consultas
class Homeadmin2(admin.ModelAdmin):
    list_display = ["id", "name", "query_type", "message"]
    search_fields= ["query_type",]
    list_per_page = 10
    list_filter=["query_type"]

admin.site.register(QueryType)
admin.site.register(Service, Homeadmin)
admin.site.register(Contact, Homeadmin2)

