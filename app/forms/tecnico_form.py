from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

class TecnicoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    nivel_id = SelectField('Nível', coerce=int, validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    senha = StringField('Senha', validators=[DataRequired()])
    confirmar_senha = StringField('Confirmar Senha', validators=[DataRequired()])
