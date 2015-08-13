# coding: utf-8
from django.test import TestCase
from model_mommy import mommy
from core.models import Event


class EventModelTest(TestCase):

    def setUp(self):
        self.event = mommy.make(Event)
        self.event.save()

    def test_event_create(self):
        self.assertEqual(self.event.pk, 1)

    def test_event_unicode(self):
        self.assertEqual(self.event.title, unicode(self.event))

