from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # for user authentication
from flask_login import LoginManager # to manage login of users (Login page)

app = Flask(__name__) # __name__ is the name of the module

app.config['SECRET_KEY'] = '3af96cc5b5b78bd436fd117d788fc578'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes