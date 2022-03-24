from flask import Blueprint, request,render_template

view=Blueprint('view',__name__,template_folder="template")

@view.route('/')
def home():
    return render_template("home.html",home={'home'})
    # return "<h1> Hello Test</h1>"