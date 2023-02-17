from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[
                        InputRequired(), DataRequired(), Email()])
    subject = StringField("Subject", validators=[InputRequired()])
    text_area = TextAreaField("Enter message here",
                              validators=[InputRequired()])
    submit_button = SubmitField("Submit")
