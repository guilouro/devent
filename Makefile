sass:
	sass --watch assets/sass/style.sass:assets/css/style.css --style compressed

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
