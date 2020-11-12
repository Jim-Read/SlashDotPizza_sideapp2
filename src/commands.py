from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Pizza import Pizza
    from faker import Faker
    faker = Faker()

    for i in range(10):
        pizza = Pizza()
        pizza.title = faker.catch_phrase()
        pizza.title = faker.catch_phrase()
        pizza.title = faker.catch_phrase()
        pizza.title = faker.catch_phrase()
        pizza.title = faker.catch_phrase()
        db.session.add(pizza)
        print(f"{i + 1} pizza record(s) created")

    db.session.commit()
    print("Tables seeded")