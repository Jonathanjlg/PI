from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class ItempecaTem(db.Model):
    __tablename__ = "itempecatem"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    hash = db.Column(db.String(40), unique=True)
    fk_orcamento_id= db.Column(db.Integer,db.ForeignKey('orcamento.id'))
    fk_peca_id= db.Column(db.Integer,db.ForeignKey('peca.id'))