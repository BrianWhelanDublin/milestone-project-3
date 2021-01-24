from hello_blog import db
from flask_mongoengine import BaseQuerySet


class User(db.Document):
    username = db.StringField(max_length=20, unique=True, required=True)
    email = db.StringField(max_length=100, unique=True, required=True)
    password = db.StringField(max_length=50)

    meta = {
        "collection": "users",
        "queryset_class": BaseQuerySet
    }
