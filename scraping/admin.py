from django.contrib import admin
from .models import City, Language, Vacancy


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass


