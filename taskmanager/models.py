# I am defining the database so need to import db from main taskmanager package
# importing the db variable with flask-sqlalchemy the db variable contains all the column types so don't need to import separately like in last project. Can just use . notation below in each table
from taskmanager import db

# create tables represented by SQLAlchemy's ORM
# catagory table
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True) # column with variable ID. Integer, auto-incrementing 1' key
    category_name = db.Column(db.String(25), unique=True, nullable=False) # string max count 25, each category must be unique and nullable = false enforces that it's a req field. 
    # links FK and cascade deletion for TASK table. 
    # relationship just links and isn't visible on the table, backref is ref it'self (lowercase), cascade finds related tasks and deletes all. Lazy can identify tasks linked to categories when quey a category alone. 
    tasks = db.relationship("Task", backref="category", cascade="all,delete", lazy=True) 


    def __repr__(self):
        # __rep__ to represent itself (self) in the form of a string
        return self.category_name

    



# task table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False) # db.text allows longer strings like a textarea
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    #bFK links to Category table (not upper and lowercase use). 
    # cascade = 1 to many relationship ( 1 category to many tasks). If category (FK) is deleted it cascades and deletes all tasks linked to it. Prevents errors
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False) 

    def __repr__(self):
        # __repr__ to represent itself in the form of a string. 0,1,2 relate to the format order, id, taskname, isurgent
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
