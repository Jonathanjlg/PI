from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Email

class EquipamentoForm(FlaskForm):
    modelo = StringField('modelo', validators=[DataRequired()])
    acessorios = StringField('acessorios', validators=[DataRequired()])
    marca_id = SelectField('Marca', coerce=int, validators=[DataRequired()])