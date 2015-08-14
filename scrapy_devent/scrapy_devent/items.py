# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from core.models import Event
from scrapy_djangoitem import DjangoItem

class EventItem(DjangoItem):
    django_model = Event
