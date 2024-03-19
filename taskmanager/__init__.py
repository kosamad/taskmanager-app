import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

# create instance of imported Flask class above stored in app variable takes the default __name__ module
app = Flask(__name__)
# specifying two app configurations from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create instance of the sqlalchemy class above and assign to varible db set to instance of flass app (above)
db = SQLAlchemy(app)

# from taskmanager package import routes (has to be here as needs app and db which are defined above)
from taskmanager import routes

#------------------------------------------------------------------------------