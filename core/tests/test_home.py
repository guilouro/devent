# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from core.models import Event
from model_mommy import mommy
from datetime import datetime, timedelta

class HomeTest(TestCase):

    def setUp(self):
        self.prev = mommy.make(
            Event,
            start_date=datetime.now() - timedelta(days=1)
        )

        self.next = mommy.make(
            Event,
            start_date=datetime.now() + timedelta(days=1)
        )

        self.resp = self.client.get(r('core:home'))

    def test_get(self):
        '''
        GET / must return status code 200
        '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''
        Home must use template index.html
        '''
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_context_event(self):
        '''
        Context event in home
        '''
        self.assertIn('events', self.resp.context)

    def test_upcomming_events(self):
        '''
        Only upcomming events
        '''
        self.assertTrue(len(self.resp.context['events']) == 1)
