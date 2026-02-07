from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FormCorsoBase(FlaskForm):
    name = StringField("Nome del corso")
    subject = StringField("Argomento")
    submit = SubmitField("Submit")
