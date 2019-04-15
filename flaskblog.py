from flask import Flask, render_template
app = Flask(__name__) # __name__ is the name of the module

# we use routes decorators to add pages to the web-
# decorators are used add additional functionalities to existing functions

# we need to set an environment variable to the file that we want to be our Flask application

@app.route("/") # "/" root/home page
def hello():
    return "<h1>Home Page</h1>"

# We can make more than one route refer to the same page
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)