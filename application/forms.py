from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    note = TextAreaField("note",validators=[DataRequired()])
    completed = SelectField("completed", choices=[("False", "False"), ("True", "True")],validators=[DataRequired()])
    submit = SubmitField("Add todo")
