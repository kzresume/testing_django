from django.contrib import admin
from .models import Candy 

@admin.register(Candy)
class CandyAdmin(admin.ModelAdmin):
    '''Admin View for Candy'''

    list_display = ('name','color')
    list_filter = ('name',)
    search_fields = ('',)
    ordering = ('name',)
