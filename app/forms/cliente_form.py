from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = StringField('telefone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cpf = StringField('CPF', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    

