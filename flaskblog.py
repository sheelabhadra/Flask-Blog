from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__) # __name__ is the name of the module

app.config['SECRET_KEY'] = '3af96cc5b5b78bd436fd117d788fc578' 

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
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)