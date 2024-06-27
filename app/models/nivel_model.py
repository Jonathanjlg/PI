from app import db

class Nivel(db.Model):
    __tablename__ = 'nivel'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # Exemplo de relacionamento com Tecnico
    tecnicos = db.relationship('Tecnico', back_populates='nivel')


