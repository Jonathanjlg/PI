from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Text

class Servico(db.Model):
    __tablename__ = "servico"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    etapa = db.Column(db.String(80))
    situacao = db.Column(Text, nullable=False)
    codigo_rastreio = db.Column(db.String(30))
    data_entrega = db.Column(db.Date)