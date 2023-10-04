from django.contrib import admin
from contact.models import Contact

# Register your models here.
# Aqui, você importa a classe Contact e registra no admin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
