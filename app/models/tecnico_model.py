# Importe as bibliotecas necessárias
from app import db
class Tecnico(db.Model):
    __tablename__ = 'tecnico'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    # Exemplo de relacionamento com Nivel
    nivel = db.relationship('Nivel', back_populates='tecnicos')

