from hello_blog import db, bcrypt
from flask_mongoengine import BaseQuerySet


# creates the User class
class User(db.Document):
    username = db.StringField(max_length=20, unique=True, required=True)
    email = db.StringField(max_length=100, unique=True, required=True)
    password = db.StringField(max_length=100)

    meta = {
        "collection": "users",
        "queryset_class": BaseQuerySet
    }

    # creates a function that uses flask-bcrypt to hash
    # the users passwords for the database
    def hash_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
