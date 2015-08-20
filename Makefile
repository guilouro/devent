sass:
	sass --watch static/sass/style.sass:static/css/style.css --style compressed

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete

migrate:
	python manage.py makemigrations
	python manage.py migrate