from app import db
from model.estado import Estado
from model.solucao import Solucao
from model.solucao_fornecedor import SolucaoFornecedor
from model.fornecedor import Fornecedor

def seed_estados():
    estados = [
        {"nome": "Acre", "sigla": "AC", "tarifa_base_kwh": 0.99},
        {"nome": "Alagoas", "sigla": "AL", "tarifa_base_kwh": 0.61},
        {"nome": "Amapá", "sigla": "AP", "tarifa_base_kwh": 0.90},
        {"nome": "Amazonas", "sigla": "AM", "tarifa_base_kwh": 0.66},
        {"nome": "Bahia", "sigla": "BA", "tarifa_base_kwh": 0.55},
        {"nome": "Ceará", "sigla": "CE", "tarifa_base_kwh": 0.86},
        {"nome": "Distrito Federal", "sigla": "DF", "tarifa_base_kwh": 0.39},
        {"nome": "Espírito Santo", "sigla": "ES", "tarifa_base_kwh": 0.72},
        {"nome": "Goiás", "sigla": "GO", "tarifa_base_kwh": 0.87},
        {"nome": "Maranhão", "sigla": "MA", "tarifa_base_kwh": 0.85},
        {"nome": "Mato Grosso", "sigla": "MT", "tarifa_base_kwh": 0.50},
        {"nome": "Mato Grosso do Sul", "sigla": "MS", "tarifa_base_kwh": 0.68},
        {"nome": "Minas Gerais", "sigla": "MG", "tarifa_base_kwh": 0.80},
        {"nome": "Pará", "sigla": "PA", "tarifa_base_kwh": 0.89},
        {"nome": "Paraíba", "sigla": "PB", "tarifa_base_kwh": 0.81},
        {"nome": "Paraná", "sigla": "PR", "tarifa_base_kwh": 0.87},
        {"nome": "Pernambuco", "sigla": "PE", "tarifa_base_kwh": 0.91},
        {"nome": "Piauí", "sigla": "PI", "tarifa_base_kwh": 0.76},
        {"nome": "Rio Grande do Norte", "sigla": "RN", "tarifa_base_kwh": 0.45},
        {"nome": "Rio Grande do Sul", "sigla": "RS", "tarifa_base_kwh": 0.59},
        {"nome": "Rio de Janeiro", "sigla": "RJ", "tarifa_base_kwh": 0.70},
        {"nome": "Rondônia", "sigla": "RO", "tarifa_base_kwh": 0.49},
        {"nome": "Roraima", "sigla": "RR", "tarifa_base_kwh": 0.54},
        {"nome": "Santa Catarina", "sigla": "SC", "tarifa_base_kwh": 0.83},
        {"nome": "Sergipe", "sigla": "SE", "tarifa_base_kwh": 0.78},
        {"nome": "São Paulo", "sigla": "SP", "tarifa_base_kwh": 0.85},
        {"nome": "Tocantins", "sigla": "TO", "tarifa_base_kwh": 0.97},
    ]

    for e in estados:
        existe = Estado.query.filter_by(sigla=e["sigla"]).first()
        if not existe:
            novo_estado = Estado(**e)
            db.session.add(novo_estado)

    db.session.commit()
    print("sucesso: estados inseridos")


def seed_solucoes():
    solucaoes = [
        {"cod": "GD", "nome": "Geração Distribuída"},
        {"cod": "ML", "nome": "Mercado Livre"},
    ]

    for s in solucaoes:
        existe = Solucao.query.filter_by(cod=s["cod"]).first()
        if not existe:
            nova_solucao = Solucao(**s)
            db.session.add(nova_solucao)
    
    db.session.commit()
    print("sucesso: soluções inseridas")


def seed_fornecedores():
    fornecedores = [
        {"nome": "Fornecedor A", "logo": "https://example.com/logo_a.png", "estado_id": 1, "total_clientes": 100, "avaliacoes_media": 4.5},
        {"nome": "Fornecedor B", "logo": "https://example.com/logo_b.png", "estado_id": 2, "total_clientes": 150, "avaliacoes_media": 4.0},
        {"nome": "Fornecedor C", "logo": "https://example.com/logo_c.png", "estado_id": 3, "total_clientes": 200, "avaliacoes_media": 4.8},
        {"nome": "Fornecedor D", "logo": "https://example.com/logo_d.png", "estado_id": 4, "total_clientes": 250, "avaliacoes_media": 4.2},
        {"nome": "Fornecedor E", "logo": "https://example.com/logo_e.png", "estado_id": 5, "total_clientes": 300, "avaliacoes_media": 4.7},
        {"nome": "Fornecedor F", "logo": "https://example.com/logo_f.png", "estado_id": 6, "total_clientes": 350, "avaliacoes_media": 4.3},
        {"nome": "Fornecedor G", "logo": "https://example.com/logo_g.png", "estado_id": 7, "total_clientes": 400, "avaliacoes_media": 4.6},
        {"nome": "Fornecedor H", "logo": "https://example.com/logo_h.png", "estado_id": 8, "total_clientes": 450, "avaliacoes_media": 4.4},
        {"nome": "Fornecedor I", "logo": "https://example.com/logo_i.png", "estado_id": 9, "total_clientes": 500, "avaliacoes_media": 4.9},
        {"nome": "Fornecedor J", "logo": "https://example.com/logo_j.png", "estado_id": 10, "total_clientes": 550, "avaliacoes_media": 4.1},

    ]

    for f in fornecedores:
        existe = Fornecedor.query.filter_by(nome=f["nome"]).first()
        if not existe:
            novo_fornecedor = Fornecedor(**f)
            db.session.add(novo_fornecedor)
    
    db.session.commit()
    print("sucesso: fornecedores inseridos")


def seed_solucao_fornecedor():
    solucao_fornecedores = [
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 1, "custo_kwh": 0.95},
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 2, "custo_kwh": 0.57},
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 3, "custo_kwh": 0.85},
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 4, "custo_kwh": 0.60},
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 5, "custo_kwh": 0.50},
        {"solucao_id": 2, "fornecedor_id": 6, "estado_id": 6, "custo_kwh": 0.80},
        {"solucao_id": 2, "fornecedor_id": 7, "estado_id": 7, "custo_kwh": 0.75},
        {"solucao_id": 2, "fornecedor_id": 8, "estado_id": 8, "custo_kwh": 0.70},
        {"solucao_id": 2, "fornecedor_id": 9, "estado_id": 9, "custo_kwh": 0.65},
        {"solucao_id": 2, "fornecedor_id": 10, "estado_id": 10, "custo_kwh": 0.55},
        {"solucao_id": 1, "fornecedor_id": 6, "estado_id": 6, "custo_kwh": 0.78},
        {"solucao_id": 1, "fornecedor_id": 7, "estado_id": 7, "custo_kwh": 0.72},
        {"solucao_id": 1, "fornecedor_id": 8, "estado_id": 8, "custo_kwh": 0.68},
        {"solucao_id": 1, "fornecedor_id": 9, "estado_id": 9, "custo_kwh": 0.63},
        {"solucao_id": 1, "fornecedor_id": 10, "estado_id": 10, "custo_kwh": 0.58},
        {"solucao_id": 2, "fornecedor_id": 1, "estado_id": 1, "custo_kwh": 0.90},
        {"solucao_id": 2, "fornecedor_id": 2, "estado_id": 2, "custo_kwh": 0.52},
        {"solucao_id": 2, "fornecedor_id": 3, "estado_id": 3, "custo_kwh": 0.80},
        {"solucao_id": 2, "fornecedor_id": 4, "estado_id": 4, "custo_kwh": 0.55},
        {"solucao_id": 2, "fornecedor_id": 5, "estado_id": 5, "custo_kwh": 0.45},
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 2, "custo_kwh": 0.92},
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 3, "custo_kwh": 0.58},
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 4, "custo_kwh": 0.82},
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 5, "custo_kwh": 0.57},
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 6, "custo_kwh": 0.48},
        {"solucao_id": 2, "fornecedor_id": 6, "estado_id": 7, "custo_kwh": 0.77},
        {"solucao_id": 2, "fornecedor_id": 7, "estado_id": 8, "custo_kwh": 0.73},
        {"solucao_id": 2, "fornecedor_id": 8, "estado_id": 9, "custo_kwh": 0.69},
        {"solucao_id": 2, "fornecedor_id": 9, "estado_id": 10, "custo_kwh": 0.64},
        {"solucao_id": 2, "fornecedor_id": 10, "estado_id": 1, "custo_kwh": 0.54},
    ]

    for sf in solucao_fornecedores:
        existe = SolucaoFornecedor.query.filter_by(solucao_id=sf["solucao_id"], fornecedor_id=sf["fornecedor_id"], estado_id=sf["estado_id"]).first()
        if not existe:
            nova_solucao_fornecedor = SolucaoFornecedor(**sf)
            db.session.add(nova_solucao_fornecedor)
    
    db.session.commit()
    print("sucesso: soluções fornecedores inseridos")