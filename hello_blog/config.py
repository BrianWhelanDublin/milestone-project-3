import os
if os.path.exists("env.py"):
    import env


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGO_DBNAME"),
        'host': os.environ.get("MOGO_URI")
        }

    CLOUD_NAME = os.environ.get("CLOUD_NAME")
    API_KEY = os.environ.get("API_KEY")
    API_SECRET = os.environ.get("API_SECRET")
