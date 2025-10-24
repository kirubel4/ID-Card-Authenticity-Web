import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'klausg00d'

    UPLOADS =""

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugCOnfig(Config):
    DEBUG = False