from flask import Flask


def create_app():
    app = Flask(__name__)

    from hello_blog.main.routes import main

    app.register_blueprint(main)

    return app
