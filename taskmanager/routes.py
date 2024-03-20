from flask import render_template
from taskmanager import app, db

# after setting up models.py file
from taskmanager.models import Category, Task 

# to get the app running create a basic app at the root-level which will be used to target a function called home and return the rendered template (base.html). 
@app.route("/")
def home():
    return render_template("tasks.html")


#------------------------------------------------------------------------------