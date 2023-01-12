from django.contrib import admin

from .models import Region, School_location, Pupil


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    search_fields = ('region',)


@admin.register(School_location)
class School_locationAdmin(admin.ModelAdmin):
    search_fields = ('location',)


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    search_fields = ('birth_date',)
    autocomplete_fields = ('studying_address',)
