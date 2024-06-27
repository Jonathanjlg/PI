from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired
class OrcamentoForm(FlaskForm):
    quantidade = StringField("quantidade",validators=[DataRequired()])
    item = StringField("item",validators=[DataRequired()])
    valor_unit = StringField("valor_unit",validators=[DataRequired()])
    observacoes = StringField("observacoes",validators=[DataRequired()])
    tecnico_id = SelectField('tecnico', coerce=int, validators=[DataRequired()])
    cliente_id = SelectField('cliente', coerce=int, validators=[DataRequired()])
    servico_id = SelectField('servico', coerce=int, validators=[DataRequired()])
    equipamento_id = SelectField('equipamento', coerce=int, validators=[DataRequired()])