from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField
from wtforms.validators import DataRequired

#our app instance
app = Flask(__name__)

# Create a secret key for form. Purpose to ensure for cant get hacked
app.config['SECRET_KEY'] = 'Password' # can be any length

#create a form class
class NamerForm(FlaskForm):
    #define what you want to use in your form
    name = SearchField("Enter your Name", validators=[DataRequired()]) #'validators' check if form is filled in w/ 'DataRequired()'
    submit = SubmitField("Submit")





#create route aka URL
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    #passing list to index "other Datastructure work the same way"
    pizza = ["Cheese", "Mushroom", "Pineapple", "chicken"]
    return render_template("user.html", user_name=name, pizza = pizza)


@app.route("/base")
def base():
    return render_template("base.html")

#create custom error page

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):#passing in e "for ERROR"
    return render_template("500.html"), 500 #corresponding erros for functions




if __name__ == '__main__':
   app.run(debug = True)

