import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        #value = os.getenv("DB_URI")
        value = "postgres+psycopg2://slash:Me1bourne1!@slashdotpizza.cwatzillm6wc.us-east-1.rds.amazonaws.com:5432/slashdotpizza"

        if not value:
            raise ValueError("DB_URI is not set!")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class  TestingConfig(Config):
    TESTING = True

environment = os.getenv("FLASK_ENV")

if environment ==  "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()

# DB_URI=slashdotpizza+psycopg2://slash:Me1bourne1!@slashdotpizza.cwatzillm6wc.us-east-1.rds.amazonaws.com:5432/slashdotpizza