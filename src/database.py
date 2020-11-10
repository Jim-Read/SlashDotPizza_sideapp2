from flask_sqlalchemy import SQLAlchemy
import os



def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{os.getenv('DB_NAME')}+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db 