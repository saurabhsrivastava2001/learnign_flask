#store the standard route for the website pages

from flask import Blueprint,render_template

#this file is the blueprint of our application , means it has some / all  routes of our application
# blueprint kind of alow us to make multipe views not all the view in the same file 

views = Blueprint('views',__name__)  # we are making ablueprint / temp view naming it as view

@views.route('/')  #whenever we are going to the root/main page
def home():        #this function is going to run
    return render_template("home.html")
