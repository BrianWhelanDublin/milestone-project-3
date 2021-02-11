import os
from hello_blog import create_app
if os.path.exists("env.py"):
    import env


# my app has been set up as an app factory in the __init__.py file
# within my appplication folder which I have named hello_blog
# I import the function create_app at the top and then call it
# in this file which then creates my app.
app = create_app()


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
