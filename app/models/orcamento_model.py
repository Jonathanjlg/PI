from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Text

class Orcamento(db.Model):
    __tablename__ = "orcamento"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    quantidade  = db.Column(db.String(50))
    item  = db.Column(db.String(50))
    valor_unit  = db.Column(db.String(30))
    observacoes = db.Column(Text, nullable=False)
    fk_tecnico_id= db.Column(db.Integer,db.ForeignKey('tecnico.id'))
    fk_cliente_id= db.Column(db.Integer,db.ForeignKey('cliente.id'))
    fk_servico_id= db.Column(db.Integer,db.ForeignKey('servico.id'))
    fk_equipamento_id= db.Column(db.Integer,db.ForeignKey('equipamento.id'))