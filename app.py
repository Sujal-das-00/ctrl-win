from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")  # Home route is now enabled
def home():
    return render_template("index.html")  # Home page

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        # You can store the user in a database here
        
        return redirect(url_for("login"))  # Redirect to login after signup
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # You can add authentication logic here (e.g., check from a database)
        
        return redirect(url_for("home"))  # Redirect to home after login
    return render_template("login.html")

@app.route("/host_ride", methods=["GET", "POST"])
def host():
    return render_template("host_ride.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
