# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    url = models.URLField(_(u'Url'), null=True, unique=True)
    title = models.CharField(_(u'Título'), max_length=200)
    image = models.URLField(_(u'Imagem'), null=True, max_length=250)
    start_date = models.DateTimeField(_(u'Começa em:'), null=True)
    local = models.CharField(_('Local'), max_length=200)
    price = models.CharField(_(u'Preço'), max_length=20, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name=_('Evento')
        verbose_name_plural=_('Eventos')