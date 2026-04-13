from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "geheim123"  # wichtig für Sessions

# Fake Benutzer (hartcodiert)
USERNAME = "admin"
PASSWORD = "1234"

@app.route("/")
def home():
    if "user" in session:
        return f"Hallo {session['user']}! <br><a href='/logout'>Logout</a>"
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        if user == USERNAME and pw == PASSWORD:
            session["user"] = user
            return redirect(url_for("home"))
        else:
            return "Falsche Daten!"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)