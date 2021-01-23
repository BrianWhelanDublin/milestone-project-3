import os
if os.path.exists("env.py"):
    import env


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
