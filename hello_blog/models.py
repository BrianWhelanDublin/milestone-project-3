from hello_blog import db, bcrypt, login_manager
from flask_mongoengine import BaseQuerySet
from flask_login import UserMixin
from datetime import datetime


# creates the User class
# Usermixin adds the basic functions needed to the userclass for flask login
class User(db.Document, UserMixin):
    username = db.StringField(max_length=20, unique=True, required=True)
    email = db.StringField(max_length=100, unique=True, required=True)
    password = db.StringField(max_length=100)
    bio = db.StringField(max_length=250)
    #  default image from cloudinary image database
    user_image = db.StringField(
        default="https://res.cloudinary.com/dmgevdb7w/image\
/upload/w_200,h_200,c_fill,g_face/v1610563923/xymcofmhj3le6l9uh8qa.jpg")
    date_joined = db.DateTimeField(default=datetime.utcnow)

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
# pk = primary key
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


# create the category class
class Categories(db.Document):
    category_name = db.StringField(max_length=20)

    meta = {
        "collection": "categories",
        "queryset_class": BaseQuerySet
    }

    def __repr__(self):
        return f"Category({self.category_name})"


# create the model class for each post
class Post(db.Document):
    title = db.StringField(max_length=50)
    category = db.ReferenceField(Categories)
    content = db.StringField()
    date_posted = db.DateTimeField(default=datetime.utcnow)
    author = db.ReferenceField(User)
    comments = db.ListField(db.ReferenceField("Comment"))

    meta = {
        "collection": "posts",
        "queryset_class": BaseQuerySet
    }

    def __repr__(self):
        return f"Post({self.title}, {self.author}, {self.date_posted})"


#  create the class for comments.
class Comment(db.Document):
    comment = db.StringField(max_length=200, required=True)
    comment_author = db.ReferenceField(User)
    post = db.ReferenceField(Post)

    metha = {
        "collection": "comments"
    }
