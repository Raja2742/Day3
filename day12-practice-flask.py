#GET

from flask import Flask

# Step 1: Create a Flask app
app = Flask(__name__)

# Step 2: Define a route (URL)
@app.route("/")
def home():
    return "Hello Raja! 🚀 This is your first Flask app."

# Step 3: Run the app
if __name__ == "__main__":
    app.run(debug=True)


# post

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/")
def form_page():
    return render_template("form.html")

@app.route("/submit", methods=["post"])
def submit():
    name=request.form.get("name","unknown")
    return f"form submited by {name}"

if __name__ == "__main__":
    app.run(debug=True)


