from types import MethodDescriptorType
from flask import Blueprint, render_template, request, flash

auth=Blueprint('auth',__name__,template_folder="template")

@auth.route('/login', methods=['GET','POST'])
def login():
    data=request.form
    print(data)
    # return "<p> Login</p>"
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method =="POST":
        email= request.form.get('email')
        firstname= request.form.get('firstname')
        password= request.form.get('password')
        cpassword= request.form.get('cpassword')
        
        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(firstname) < 2:
            flash("Firstname must be greater than 4 characters.", category="error")
        elif len(password) != len(cpassword):
            flash("Password not match.", category="error")
        elif len(password) < 7:
            flash("Password must be greater than 4 characters.", category="error")
        else:
            # Add user to database
            flash("User register successful.", category="successful")        
    
    return render_template('signup.html')