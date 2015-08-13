# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    title = models.CharField(_(u'Título'), max_length=200)
    from_day = models.DateTimeField(_('De'))
    to_day = models.DateTimeField(_('To'))
    local = models.CharField(_('Local'), max_length=200)
    address = models.CharField(_('Endereço'), max_length=200)
    price = models.CharField(_(u'Preço'), max_length=20)
