from django.contrib import admin

from .models import Personals


@admin.register(Personals)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position']

    @admin.display(ordering='first_name')
    def full_name(self, personal):
        return f"{personal.first_name} {personal.last_name}"

