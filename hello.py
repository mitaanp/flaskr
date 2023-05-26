from flask import Flask, render_template

#Creating a flask instance

app = Flask(__name__)
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


