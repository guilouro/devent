# coding: utf-8
from django.shortcuts import render
from core.models import Event
from datetime import datetime, timedelta


def home(request):
    events = Event.objects.filter(
        start_date__gt=datetime.now() - timedelta(hours=5))
    return render(request, 'core/index.html', {'events': events})
