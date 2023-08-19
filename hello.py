from flask import Flask, render_template

#our app instance
app = Flask(__name__)


#create route aka URL
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    #passing list to index "other Datastructure work the same way"
    pizza = ["Cheese", "Mushroom", "Pineapple", "chicken"]
    return render_template("user.html", user_name=name, pizza = pizza)

#create custom error page

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500





if __name__ == '__main__':
   app.run(debug = True)

