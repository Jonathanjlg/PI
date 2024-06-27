from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class ServicoForm(FlaskForm):
    etapa = StringField("etapa",validators=[DataRequired()])
    situacao = StringField("situação",validators=[DataRequired()])
    codigo_rastreio = StringField("Codigo",validators=[DataRequired()])
    data_entrega = StringField("data_entrega",validators=[DataRequired()])
    
   