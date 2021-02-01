import os
import cloudinary
if os.path.exists("env.py"):
    import env


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGO_DBNAME"),
        'host': os.environ.get("MONGO_URI")
    }

    cloudinary.config(
        cloud_name=os.environ.get("CLOUD_NAME"),
        api_key=os.environ.get("API_KEY"),
        api_secret=os.environ.get("API_SECRET")
    )

    # SEND_FILE_MAX_AGE_DEFAULT = 0
