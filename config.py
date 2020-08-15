
class Config:

    TESTING = False
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    DEBUG = True


class ProductionConfig(Config):

    DEBUG = False
    

class TestingConfig(Config):

    TESTING = True


app_config = {
    'development' : DevelopmentConfig,
    'production' :  ProductionConfig,
    'testing' : TestingConfig
}

