from flask import Flask, jsonify

app = Flask(__name__)

votes = {}


@app.route("/")
def home():
    return "Welcome to the App"


@app.route("/health")
def health():
    return "App is running"


if __name__ == "__main__":
    app.run(debug=True)