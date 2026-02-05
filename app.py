from flask import Flask

app = Flask(__name__)

# Rotte
@app.route("/")
def index():
    wow = "bello"
    return f"<h1>Ciao, {wow} mondo!</h1>"

@app.route("/info")
def info():
    return "<h2>Queste sono un sacoo di informazioni!</h2>"


@app.route("/info/<name>") # 127.0.0.1:5000/info/andrea
def nome_ok(name):
    return f"<h2>Il mio nome: {name}</h2>"

# Facciamo scattare un errore
@app.route("/info-errore/<name>")
def errore(name):
    return f"<h2>Generiamo un errore: </h2>".format(name[50])

# Avviare l'applicazione
if __name__ == "__main__":
    app.run(debug=True)