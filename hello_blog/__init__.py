from flask import Flask


def create_app():
    app = Flask(__name__)

    from hello_blog.main.routes import main
    from hello_blog.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
