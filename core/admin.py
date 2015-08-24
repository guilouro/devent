# coding: utf-8

from django.contrib import admin
from core.models import Event


class EventAdmin(admin.ModelAdmin):

    items = (
        'title', 'local', 'price', 'start_date', 'created_at',
    )

    list_display = items
    search_display = items
    date_hierarchy = 'start_date'
    list_filter = ['start_date']


admin.site.register(Event, EventAdmin)
