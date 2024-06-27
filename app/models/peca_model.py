from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Peca(db.Model):
    __tablename__ = "peca"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(80))
    marca = db.Column(db.String(50))
    quantidade  =  db.Column(db.Integer)