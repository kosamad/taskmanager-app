from flask import render_template, request, redirect, url_for
from taskmanager import app, db

# after setting up models.py file
from taskmanager.models import Category, Task 

# to get the app running create a basic app at the root-level which will be used to target a function called home and return the rendered template (base.html). 
# tasks variable is created later to view tasks as is, tasks=tasks
@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all()) # converting database queries into python lists
    return render_template("tasks.html",tasks=tasks) #task=task passes list to front end template


#------------------------------------------------------------------------------

@app.route("/categories")
def categories(): # remember this is calling the python function not the app.route
    # query the Category model. order_by req to stop order being by 1' key. This will happen whenever you navigate to the categories page. 
    categories = list(Category.query.order_by(Category.category_name).all())
    #categories.categories added with query. Uses data to display to user. This is a cursor object therefore req list above
    #1st categories comes from variable name within html template, the 2nd is the list defined above in the function
    return render_template("categories.html", categories=categories) 


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

# this function handles the editing capability. When a variable is passed back into the function it needs <> cast as an int as 1' = an integer
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # so the route directory knows which catagory to load. if it can't find the spec record it triggers a 404 error page
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name") # update category name, then commit the session to database and redirect
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    # specify which category we want to delete (uses same functionality to above to find the category)
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories")) # redirect to catagories function above


@app.route("/add_task", methods=["GET", "POST"])
def add_task():    
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task=Task(
        task_name=request.form.get("task_name"),
        task_description=request.form.get("task_description"),
        is_urgent=bool(True if request.form.get("is_urgent") else False),
        due_date=request.form.get("due_date"),
        category_id=request.form.get("category_id")
        )       
        db.session.add(task)
        db.session.commit()      
        return redirect(url_for("home"))
    return render_template("add_task.html", categories = categories) # second argument gives a dropdown list to display available catagories (see above for where come from)

@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"]) # need to know which task want to edit so task ID(as an int) is in the app root URL
def edit_task(task_id): #and task_id is here too
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        # Update each column using . notation. Important to do for all tasks otherwise they might be deleted (when a user only updates 1 field)
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(request.form.get("is_urgent"))
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()       
    return render_template("edit_task.html", task=task, categories=categories)# second argument gives a dropdown list to display available catagories and tasks 

# takes task_id variable and then query's the database to find that task. Then it removes it using the delete() method and commits the changes. 
@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    # specify which task we want to delete (uses same functionality to above to find the category)
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home")) # redirect to home