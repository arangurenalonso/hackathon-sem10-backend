from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Enviar')
