from flask import render_template
from taskmanager import app, db

# to get the app running create a basic app at the root-level which will be used to target a function called home and return the rendered template (base.html). 
@app.route("/")
def home():
    return render_template("base.html")


#------------------------------------------------------------------------------