web: gunicorn devent.wsgi
worker: python manage.py celeryd_detach worker -B -l info
