from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Cliente(db.Model):
    __tablename__ = "cliente"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(80))
    cpf = db.Column(db.String(20))
    telefone  = db.Column(db.String(20))
    email  = db.Column(db.String(30))
