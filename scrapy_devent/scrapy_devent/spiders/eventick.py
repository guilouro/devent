# coding: utf-8

import scrapy
from dateutil import parser
from scrapy_devent.items import EventItem


class EventickSpider(scrapy.Spider):
    tags = [
        'developer', 'python', 'developer', 'frontend', 'front-end',
        'hackathon', 'php', 'javascript', 'node'
    ]
    name = 'eventick'
    hostname = 'https://www.eventick.com.br'
    start_urls = [
        "%s/eventos?q=%s&all=false" % (hostname, t) for t in tags]

    def parse(self, response):
        for item in response.xpath('//*[@id="events-form"]/section[2]/ul/li'):
            url = item.xpath('descendant::a/@href').extract_first()
            meta = {
                'title': item.xpath(
                    'descendant::h5[2]/text()').extract_first(),
                'image': item.xpath(
                    'descendant::img/@src').extract_first(),
                'local': item.xpath(
                    'descendant::span[@itemprop="location"]/span/text()'
                ).extract_first(),
                'start_date': item.xpath(
                    'descendant::span[@itemprop="startDate"]/@content'
                ).extract_first(),
            }

            yield scrapy.Request(
                '%s%s' % (self.hostname, url),
                meta=meta,
                callback=self.parse_event
            )

    def parse_event(self, response):
        event = EventItem()
        event['url'] = response.url
        event['title'] = response.meta['title']
        event['image'] = response.meta['image']
        event['local'] = response.meta['local']
        event['start_date'] = parser.parse(response.meta['start_date'])
        event['price'] = response.xpath(
            '(//td[@class="total"])[last()]//text()').extract_first()
        yield event
