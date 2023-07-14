from os import environ, path

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    

class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    
class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True

