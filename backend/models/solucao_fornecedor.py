from app import db

class SolucaoFornecedor(db.Model):
    __tablename__ = 'solucao_fornecedor'
    __table_args__ = (db.UniqueConstraint('solucao_id', 'fornecedor_id', 'estado_id', name='uq_solucao_fornecedor_estado'),)

    id = db.Column(db.Integer, primary_key=True)
    solucao_id = db.Column(db.Integer, db.ForeignKey('solucoes.id', ondelete='CASCADE'), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id', ondelete='CASCADE'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id', ondelete='CASCADE'), nullable=False)
    custo_kwh = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<SoluçãoFornecedor Solução ID: {self.solucao_id}, Fornecedor ID: {self.fornecedor_id}>"