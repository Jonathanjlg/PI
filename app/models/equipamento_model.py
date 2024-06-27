from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Equipamento(db.Model):
    __tablename__ = "equipamento"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    modelo  = db.Column(db.String(80))
    acessorios = db.Column(db.String(200))
    fk_marca_id= db.Column(db.Integer,db.ForeignKey('marca.id'))