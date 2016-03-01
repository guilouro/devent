from .settings import *

DATABASES = {
    'default': parse('sqlite:///' + BASE_DIR.child('db.sqlite3'))
}
