from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

"""Environment Configurations"""
class BaseConfig(object):
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    ENV = 'testing'
    DEBUG = False
    TESTING = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    TESTING = False
