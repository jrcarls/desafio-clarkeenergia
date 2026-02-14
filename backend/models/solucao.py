from app import db

class Solucao(db.Model):
    __tablename__ = 'solucoes'

    id = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.String(20), nullable=False, unique=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)

    fornecedores = db.relationship('SolucaoFornecedor', backref='solucao', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Solução {self.nome}>"