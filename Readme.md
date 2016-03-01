[![Build Status](https://travis-ci.org/guilouro/devent.svg?branch=master)](https://travis-ci.org/guilouro/devent)

Devent
=======
Projeto hospedado em [http://devent.herokuapp.com](http://devent.herokuapp.com) feito para estudo de integração do Django + Celery + Scrapy.

Sua finalidade é buscar os próximos eventos de desenvolvimento, através da plataforma [Eventick](http://eventick.com.br).

### Como testar

#### Crie e ative um ambiente virtual
```
$ virtualenv devent
$ cd devent
$ source bin/activate
```

#### Faça o clone do projeto
```
$ git clone https://github.com/guilouro/devent.git
$ cd devent/
$ make
```

#### Buscar novos eventos
```
$ make crawl
```

#### Server
```
$ make run
```
