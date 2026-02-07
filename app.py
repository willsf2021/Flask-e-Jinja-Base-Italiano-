from flask import Flask, render_template, request, url_for

app = Flask(__name__)


# Rotta Iniziale
@app.route("/")
def index():
    return render_template("index.html")


# Gestori di Errori
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# Rotte Diversi
@app.route("/course/new/")
def new_course():
    context = {}

    args_keys = ["course-name", "course-subject"]

    for arg in request.args:
        if arg in args_keys:
            key_context = str(arg.replace("-", "_"))
            context[key_context] = request.args.get(arg)

    # Oppure (Per questo devi conocescere list and dict comprehension):
    
    # context.update(
    #     {
    #         arg.replace("-", "_"): request.args.get(arg)
    #         for arg in request.args
    #         if arg in args_keys
    #     }
    # )
    
   

    return render_template("course_new.html", context=context)


@app.route("/course/created")
def course_created():
    context = {}
    context["course_name"] = "nulla"
    context["course_subject"] = "nulla"

    return render_template("course_created.html", context=context)


# Avviare l'applicazione
if __name__ == "__main__":
    app.run(debug=True)
