from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Marca(db.Model):
    __tablename__ = "marca"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(80))