from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! This is the home page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

if __name__ == "__main__":
	app.run()
