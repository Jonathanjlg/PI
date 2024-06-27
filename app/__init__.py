#importando o flask
from flask import Flask
#importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_wtf import CSRFProtect

#criando o aplicativo
app = Flask(__name__)
#puxando o arquivo config.py
app.config.from_object('config')
#criando um objeto db da classe SQLAlchemy
db = SQLAlchemy(app)
#criar uma variável migrate e passar a instância da aplicação e do db
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
csrf.init_app(app)


#FIXME:model
from app.models import cliente_model
from app.models import equipamento_model
from app.models import marca_model
from app.models import nivel_model
from app.models import orcamento_model
from app.models import peca_model
from app.models import sevico_model
from app.models import tecnico_model


#FIXME:view
from .views import nivel_view
from .views import equipamento_view
from .views import orcamento_view
from .views import marca_view
from .views import cliente_view
from .views import tecnico_view



 





