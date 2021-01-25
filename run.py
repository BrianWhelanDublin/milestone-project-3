import os
from hello_blog import create_app
if os.path.exists("env.py"):
    import env


app = create_app()


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
