sass:
	sass --watch assets/sass/style.sass:assets/css/style.css --style compressed

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete

migrate:
	python manage.py makemigrations
	python manage.py migrate

crawl:
	cd scrapy_devent/scrapy_devent && scrapy list | xargs -n 1 scrapy crawl
