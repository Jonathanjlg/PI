from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class PecaForm(FlaskForm):
    nome = StringField("nome",validators=[DataRequired()])
    marca = StringField("marca",validators=[DataRequired()])
    quantidade = StringField("quantidade",validators=[DataRequired()])
   