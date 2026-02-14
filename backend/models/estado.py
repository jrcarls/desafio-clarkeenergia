from app import db

class Estado(db.Model):
    __tablename__ = 'estados'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(2), nullable=False)
    tarifa_base_kwh = db.Column(db.Float, nullable=False)

    fornecedores = db.relationship('Fornecedor', backref='estado', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Estado {self.nome} ({self.sigla})>"
