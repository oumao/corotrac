
class Config:

    TESTING = False
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):

    ENV = 'production'
    DEBUG = False
    

class TestingConfig(Config):

    ENV = 'testing'
    TESTING = True


app_config = {
    'development' = DevelopmentConfig,
    'production' =  ProductionConfig,
    'testing' = TestingConfig
}

