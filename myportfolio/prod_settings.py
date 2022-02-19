import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(find_dotenv())

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ["151.248.125.15","sixg.ru","localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}