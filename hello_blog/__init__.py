from flask import Flask
from hello_blog.config import Config
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import cloudinary

# create instances of imported extensions
db = MongoEngine()
bcrypt = Bcrypt()
login_manager = LoginManager()
# user will be redirected here if the try to accsess a page
# with login_required and they havent logged in
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


# cretes the app using the details from the config class in the config.py file
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init the extention instances to bind them to the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # set up cloudinary configuration from the confifg file
    cloudinary.config(
        cloud_name=Config.CLOUD_NAME,
        api_key=Config.API_KEY,
        api_secret=Config.API_SECRET
        )

    # imports the blueprints from each view file
    from hello_blog.main.main_views import main
    from hello_blog.users.users_views import users

    #  register each blueprint to connect it with the app
    app.register_blueprint(main)
    app.register_blueprint(users)

    # then return the app which will run when the create_app
    # function is called in run.py
    return app
