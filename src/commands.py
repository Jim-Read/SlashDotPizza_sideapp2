from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Pizza import Pizza
    from models.User import User
    from models.Comments import Comments
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()
    users = []
    pizzas = []

    #create a user table and add in 5 users to test
    for i in range(5):
        user = User()
        user.email =  f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        user.user_name = f"test{i}"
        db.session.add(user)
        users.append(user)
    
    db.session.commit()

    #create table to contain pizzas - randomlyh created with random text - users cant crete pizza - 
    for i in range(10):
        pizza = Pizza()
        pizza.pizza_name = faker.catch_phrase()
        pizza.description = faker.catch_phrase()
        pizza.price = 20
        pizza.location = faker.catch_phrase()
        #pizza.user_id = random.choice(users).user_id
        db.session.add(pizza)
        pizzas.append(pizza)

        print(f"{i + 1} pizza record(s) created")

    db.session.commit()

    #create a table test for comments - random pizzas assigned comment from random users
    for i in range(10):
        comment = Comments()

        comment.pizza_id = random.choice(pizzas).pizza_id
        comment.user_id = random.choice(users).user_id
        comment.comment = faker.catch_phrase()
        db.session.add(comment)
        print(f"{i + 1} comments created")


    db.session.commit()
    print("Tables seeded")