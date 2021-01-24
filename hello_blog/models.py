from hello_blog import db, bcrypt, login_manager
from flask_mongoengine import BaseQuerySet
# Usermixin adds the basic functions needed to the userclass for flask login
from flask_login import UserMixin


# creates the User class
class User(db.Document, UserMixin):
    username = db.StringField(max_length=20, unique=True, required=True)
    email = db.StringField(max_length=100, unique=True, required=True)
    password = db.StringField(max_length=100)

    meta = {
        "collection": "users",
        "queryset_class": BaseQuerySet
    }

    # returns the users usename and email for the class instances
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

    # creates a function that uses flask-bcrypt to hash-
    # - the users passwords for the database
    def hash_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")


# create the login_manager decorated function needed for flask login
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()
