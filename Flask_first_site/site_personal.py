from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/physics")
def physics():
    return render_template("physics.html")

@app.route("/user/<username>")
def user(username):
    return render_template("user.html",username= username)
if __name__ == "__main__":
    app.run(debug=True)