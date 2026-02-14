from app import db

class Solucao(db.Model):
    __tablename__ = 'solucoes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Solução {self.nome}>"