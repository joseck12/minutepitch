import os

class Config:
    '''
    Docstring goes here
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joseck:newpassword@localhost/watchlist'
    SECRET_KEY = os.environ['SECRET_KEY']

class ProdConfig(Config):
    '''
    Docstring goes here
    '''
    pass

class DevConfig(Config):
    '''
    Docstring goes here
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
