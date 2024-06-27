from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired
class ItempecaForm(FlaskForm):
    orcamento_id = SelectField('Orcamento', coerce=int, validators=[DataRequired()])
    peca_id = SelectField('Peca', coerce=int, validators=[DataRequired()])
   