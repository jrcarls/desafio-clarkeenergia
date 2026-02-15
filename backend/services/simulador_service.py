from models.estado import Estado
from models.solucao_fornecedor import SolucaoFornecedor

def simular_economia(estado_id, consumo_kwh):
    estado = Estado.query.filter_by(id=estado_id).first()

    if not estado:
        return {"erro": "Estado não encontrado"}

    custo_base = consumo_kwh * estado.tarifa_base_kwh

    solucoes_fornecedor = SolucaoFornecedor.query.filter_by(estado_id=estado.id).all()

    resultado = []

    for sf in solucoes_fornecedor:
        
        fornecedor = sf.fornecedor  # (relacionaento) backref para acessar o fornecedor relacionado

        solucao = sf.solucao # (relacionamento) backref para acessar a solucao relacionada

        custo_fornecedor = consumo_kwh * sf.custo_kwh
        economia = custo_base - custo_fornecedor
        economia_percentual = (economia / custo_base * 100) if custo_base > 0 else 0
        
        resultado.append({
            "nome": fornecedor.nome,
            "logo": fornecedor.logo,
            "estado_origem": fornecedor.estado.nome,
            "tipo_solucao": solucao.nome,
            "custo_kwh": sf.custo_kwh,
            "numero_clientes": fornecedor.total_clientes,
            "avaliacao_media": fornecedor.avaliacoes_media,
            "custo_base": custo_base,
            "custo_fornecedor": custo_fornecedor,
            "economia": economia,
            "economia_percentual": economia_percentual
        })
    
    return resultado