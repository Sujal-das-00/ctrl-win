#initial test

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
    return render_tfrom flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "vpool"

mysql = MySQL(app)

# Home Route
@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, from_destination, to_destination, gender FROM rides")
    rides = cur.fetchall()
    cur.close()
    
    return render_template("index.html", rides=rides)  



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, password))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for("login"))
    
    return render_template("signup.html")

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        
        if user:
            return redirect(url_for("home"))  
        else:
            return render_template("login.html", error="Invalid username or password!")
    return render_template("login.html")


@app.route("/ride/<int:ride_id>")
def ride_details(ride_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rides WHERE id = %s", (ride_id,))
    ride = cur.fetchone()
    cur.close()

    if not ride:
        return "Ride not found", 404

    return render_template("ride_details.html", ride=ride)


@app.route("/host_ride", methods=["GET", "POST"])
def host():
    return render_template("host_ride.html")





@app.route("/submit_ride", methods=["POST"])
def submit_ride():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        passenger_preference = request.form.get("passenger_preference")
        mobile = request.form.get("mobile")
        
        
        date = request.form.get("date")
        time = request.form.get("time")
        date_time = f"{date} {time}"  
        
        from_destination = request.form.get("from_destination")
        to_destination = request.form.get("to_destination")
        cost = request.form.get("cost")
        preference = request.form.get("preference")
        luggage = request.form.get("luggage")
        notes = request.form.get("notes")

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO rides (name, age, gender, passenger_preference, mobile, date_time, 
            from_destination, to_destination, cost, preference, luggage, notes) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, age, gender, passenger_preference, mobile, date_time,
              from_destination, to_destination, cost, preference, luggage, notes))

        mysql.connection.commit()
        cur.close()

        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
emplate("host_ride.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
