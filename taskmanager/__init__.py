import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

# create instance of imported Flask class above stored in app variable takes the default __name__ module
app = Flask(__name__)
# specifying two app configurations from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

#if/else statement req for Heroku build/deployment. Add at end
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABSE_URL")
    if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
     app.config["SQLALCHEMY_DATABASE_URI"] = uri

# create instance of the sqlalchemy class above and assign to varible db set to instance of flass app (above)
db = SQLAlchemy(app)

# from taskmanager package import routes (has to be here as needs app and db which are defined above)
from taskmanager import routes

#------------------------------------------------------------------------------