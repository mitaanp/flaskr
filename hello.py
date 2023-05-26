from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

secret_key = os.urandom(24)
#Creating a flask app instance
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator
@app.route('/')

def index():
    first_name = "John"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese", 32, "Mushroom"]
    return render_template("index.html", first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages

#Invalid URL - just adding more text and pushing to git to test
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500





