from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    wow = "bello"
    return f"<h1>Ciao, {wow} mondo!</h1>"


if __name__ == "__main__":
    app.run()