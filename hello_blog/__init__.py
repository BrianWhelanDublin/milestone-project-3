from flask import Flask
from hello_blog.config import Config
from flask_mongoengine import MongoEngine


# create instances of imported extensions
db = MongoEngine()


# cretes the app using the details from the config class in the config.py file
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init the extention instances to bind them to the app
    db.init_app(app)

    #  imports the blueprints from each route file
    from hello_blog.main.routes import main
    from hello_blog.users.routes import users

    #  register each blueprint to connect it with the app
    app.register_blueprint(main)
    app.register_blueprint(users)

    # then return the app which will run when the create_app
    # function is called in run.py
    return app
