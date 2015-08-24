from celery import task
from scrapy.cmdline import execute
import sys


@task()
def crawl():
    return sys.exit(execute(['scrapy', 'crawl', 'eventick']))