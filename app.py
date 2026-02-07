from flask import Flask, render_template, url_for

app = Flask(__name__)


# Rotte
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/esempio/")
def esempio_jinja():
    return render_template("flask.html")


@app.route("/info/")
def info():
    return "<h2>Queste sono un sacoo di informazioni!</h2>"


@app.route("/info/<name>")  # 127.0.0.1:5000/info/andrea
def nome_ok(name):
    return f"<h2>Il mio nome: {name}</h2>"


# Facciamo scattare un errore
@app.route("/info-errore/<name>")
def errore(name):
    return f"<h2>Generiamo un errore: </h2>".format(name[50])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/course/flask/")
def course_flask():
    context = {}
    context["nome_corso"] = "Flask"

    context["corsi"] = ["Introduzione", "Jinja avanzato"]

    return render_template("corso-flask.html", context=context)


# Avviare l'applicazione
if __name__ == "__main__":
    app.run(debug=True)
