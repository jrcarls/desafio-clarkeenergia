from app import db

class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(255), nullable=True)
    total_clientes = db.Column(db.Integer, nullable=False)
    avaliacoes_media = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Fornecedor {self.nome}"