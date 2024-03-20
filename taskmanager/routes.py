from flask import render_template, request, redirect, url_for
from taskmanager import app, db

# after setting up models.py file
from taskmanager.models import Category, Task 

# to get the app running create a basic app at the root-level which will be used to target a function called home and return the rendered template (base.html). 
@app.route("/")
def home():
    return render_template("tasks.html")


#------------------------------------------------------------------------------

@app.route("/categories")
def categories(): # remember this is calling the python function not the app.route
    return render_template("categories.html")


# function name matches what was added to the link href on the add category button.
#  when button clicks is renders the add-category template that has a form (return render_template etc), displaying it uses the get method, when the form is submited it will use the POST
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    #if requested method is post, create a new variable which is set to a new instance of the Category() model imported at the top of the file.
    if request.method == "POST":
        category = Category(category_name =request.form.get("category_name")) #category_name comes from the models.py file. Using the form to retrieve the name attribute (matches that of database model)
        # add and commiting information to sqlalchemy database varibale of db
        db.session.add(category)
        db.session.commit()
        # redirect theuser back to the categories page using redirect and url_for (both need to be imported from flask above)
        return redirect(url_for("categories"))
    return render_template("add_category.html") # this behaves as the else (the default condition)

# The above could be put into two separate functions also in real world would want to add some defensive programming and handling errors. 