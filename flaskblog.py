from flask import Flask
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
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
	app.run(debug=True)