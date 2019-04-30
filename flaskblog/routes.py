from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# posts is a list of dictionary; there is one dictionarity for each blog post
posts = [
    {
        'author': 'Sheel Dey',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 14, 2019'
    },
    {
        'author': 'Sheel Dey',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 15, 2019'
    }
]

# we use routes decorators to add pages to the web-
# decorators are used add additional functionalities to existing functions

# we need to set an environment variable to the file that we want to be our Flask application

@app.route("/") # "/" root/home page
# We can make more than one route refer to the same page
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
