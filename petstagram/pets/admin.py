from django.contrib import admin

from petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'personal_photo', 'date_of_birth', 'slug')
    list_filter = ('name', 'date_of_birth')
    search_fields = ('name', 'date_of_birth')
