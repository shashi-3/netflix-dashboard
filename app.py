from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/homepage", methods=['GET'])
def home():
    return "<h1>WELCOME TO HOME PAGE!</h1> <a href='/user-profile'> user profile</a>"

@app.route("/user-profile", methods=['GET'])
def profile():
    return "<p>WELCOME TO User Profile!</p>"

if __name__ =="main":
    app.run(port=5000, host="0.0.0.0", debug=True)