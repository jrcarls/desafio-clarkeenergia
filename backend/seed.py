from app import db
from models.estado import Estado
from models.solucao import Solucao
from models.solucao_fornecedor import SolucaoFornecedor
from models.fornecedor import Fornecedor

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
        {"nome": "SolarVerde Energia", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=SolarVerde", "estado_origem_id": 1, "total_clientes": 1200, "avaliacoes_media": 4.5},
        {"nome": "EcoWatts Brasil", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=EcoWatts", "estado_origem_id": 2, "total_clientes": 850, "avaliacoes_media": 4.0},
        {"nome": "LuzNova Soluções", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=LuzNova", "estado_origem_id": 3, "total_clientes": 2100, "avaliacoes_media": 4.8},
        {"nome": "PowerTech Energia", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=PowerTech", "estado_origem_id": 4, "total_clientes": 1650, "avaliacoes_media": 4.2},
        {"nome": "VentusForce", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=VentusForce", "estado_origem_id": 5, "total_clientes": 980, "avaliacoes_media": 4.7},
        {"nome": "BioEnergia Prime", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=BioEnergia", "estado_origem_id": 6, "total_clientes": 1450, "avaliacoes_media": 4.3},
        {"nome": "Eletron Sustentável", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=Eletron", "estado_origem_id": 7, "total_clientes": 2300, "avaliacoes_media": 4.6},
        {"nome": "GreenPower Sul", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=GreenPower", "estado_origem_id": 8, "total_clientes": 1800, "avaliacoes_media": 4.4},
        {"nome": "SunRise Energia", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=SunRise", "estado_origem_id": 9, "total_clientes": 3200, "avaliacoes_media": 4.9},
        {"nome": "AmpereVolt Solutions", "logo": "https://api.dicebear.com/7.x/shapes/svg?seed=AmpereVolt", "estado_origem_id": 10, "total_clientes": 1100, "avaliacoes_media": 4.1},
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
        # Estado 1 (AC) - tarifa: 0.99
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 1, "custo_kwh": 0.79},
        {"solucao_id": 2, "fornecedor_id": 1, "estado_id": 1, "custo_kwh": 0.74},
        {"solucao_id": 2, "fornecedor_id": 10, "estado_id": 1, "custo_kwh": 0.84},
        
        # Estado 2 (AL) - tarifa: 0.61
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 2, "custo_kwh": 0.49},
        {"solucao_id": 2, "fornecedor_id": 2, "estado_id": 2, "custo_kwh": 0.46},
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 2, "custo_kwh": 0.52},
        
        # Estado 3 (AP) - tarifa: 0.90
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 3, "custo_kwh": 0.72},
        {"solucao_id": 2, "fornecedor_id": 3, "estado_id": 3, "custo_kwh": 0.68},
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 3, "custo_kwh": 0.76},
        
        # Estado 4 (AM) - tarifa: 0.66
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 4, "custo_kwh": 0.53},
        {"solucao_id": 2, "fornecedor_id": 4, "estado_id": 4, "custo_kwh": 0.50},
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 4, "custo_kwh": 0.56},
        
        # Estado 5 (BA) - tarifa: 0.55
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 5, "custo_kwh": 0.44},
        {"solucao_id": 2, "fornecedor_id": 5, "estado_id": 5, "custo_kwh": 0.41},
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 5, "custo_kwh": 0.47},
        
        # Estado 6 (CE) - tarifa: 0.86
        {"solucao_id": 2, "fornecedor_id": 6, "estado_id": 6, "custo_kwh": 0.65},
        {"solucao_id": 1, "fornecedor_id": 6, "estado_id": 6, "custo_kwh": 0.69},
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 6, "custo_kwh": 0.73},
        
        # Estado 7 (DF) - tarifa: 0.39
        {"solucao_id": 2, "fornecedor_id": 7, "estado_id": 7, "custo_kwh": 0.29},
        {"solucao_id": 1, "fornecedor_id": 7, "estado_id": 7, "custo_kwh": 0.31},
        {"solucao_id": 2, "fornecedor_id": 6, "estado_id": 7, "custo_kwh": 0.33},
        
        # Estado 8 (ES) - tarifa: 0.72
        {"solucao_id": 2, "fornecedor_id": 8, "estado_id": 8, "custo_kwh": 0.54},
        {"solucao_id": 1, "fornecedor_id": 8, "estado_id": 8, "custo_kwh": 0.58},
        {"solucao_id": 2, "fornecedor_id": 7, "estado_id": 8, "custo_kwh": 0.61},
        
        # Estado 9 (GO) - tarifa: 0.87
        {"solucao_id": 2, "fornecedor_id": 9, "estado_id": 9, "custo_kwh": 0.65},
        {"solucao_id": 1, "fornecedor_id": 9, "estado_id": 9, "custo_kwh": 0.70},
        {"solucao_id": 2, "fornecedor_id": 8, "estado_id": 9, "custo_kwh": 0.74},
        
        # Estado 10 (MA) - tarifa: 0.85
        {"solucao_id": 2, "fornecedor_id": 10, "estado_id": 10, "custo_kwh": 0.64},
        {"solucao_id": 1, "fornecedor_id": 10, "estado_id": 10, "custo_kwh": 0.68},
        {"solucao_id": 2, "fornecedor_id": 9, "estado_id": 10, "custo_kwh": 0.72},
        
        # Estado 11 (MT) - tarifa: 0.50
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 11, "custo_kwh": 0.40},
        {"solucao_id": 2, "fornecedor_id": 2, "estado_id": 11, "custo_kwh": 0.38},
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 11, "custo_kwh": 0.42},
        
        # Estado 12 (MS) - tarifa: 0.68
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 12, "custo_kwh": 0.54},
        {"solucao_id": 2, "fornecedor_id": 5, "estado_id": 12, "custo_kwh": 0.51},
        {"solucao_id": 1, "fornecedor_id": 6, "estado_id": 12, "custo_kwh": 0.58},
        
        # Estado 13 (MG) - tarifa: 0.80
        {"solucao_id": 1, "fornecedor_id": 7, "estado_id": 13, "custo_kwh": 0.64},
        {"solucao_id": 2, "fornecedor_id": 8, "estado_id": 13, "custo_kwh": 0.60},
        {"solucao_id": 1, "fornecedor_id": 9, "estado_id": 13, "custo_kwh": 0.68},
        
        # Estado 14 (PA) - tarifa: 0.89
        {"solucao_id": 1, "fornecedor_id": 10, "estado_id": 14, "custo_kwh": 0.71},
        {"solucao_id": 2, "fornecedor_id": 1, "estado_id": 14, "custo_kwh": 0.67},
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 14, "custo_kwh": 0.75},
        
        # Estado 15 (PB) - tarifa: 0.81
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 15, "custo_kwh": 0.65},
        {"solucao_id": 2, "fornecedor_id": 4, "estado_id": 15, "custo_kwh": 0.61},
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 15, "custo_kwh": 0.69},
        
        # Estado 16 (PR) - tarifa: 0.87
        {"solucao_id": 1, "fornecedor_id": 6, "estado_id": 16, "custo_kwh": 0.70},
        {"solucao_id": 2, "fornecedor_id": 7, "estado_id": 16, "custo_kwh": 0.65},
        {"solucao_id": 1, "fornecedor_id": 8, "estado_id": 16, "custo_kwh": 0.74},
        
        # Estado 17 (PE) - tarifa: 0.91
        {"solucao_id": 1, "fornecedor_id": 9, "estado_id": 17, "custo_kwh": 0.73},
        {"solucao_id": 2, "fornecedor_id": 10, "estado_id": 17, "custo_kwh": 0.68},
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 17, "custo_kwh": 0.77},
        
        # Estado 18 (PI) - tarifa: 0.76
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 18, "custo_kwh": 0.61},
        {"solucao_id": 2, "fornecedor_id": 3, "estado_id": 18, "custo_kwh": 0.57},
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 18, "custo_kwh": 0.65},
        
        # Estado 19 (RN) - tarifa: 0.45
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 19, "custo_kwh": 0.36},
        {"solucao_id": 2, "fornecedor_id": 6, "estado_id": 19, "custo_kwh": 0.34},
        {"solucao_id": 1, "fornecedor_id": 7, "estado_id": 19, "custo_kwh": 0.38},
        
        # Estado 20 (RS) - tarifa: 0.59
        {"solucao_id": 1, "fornecedor_id": 8, "estado_id": 20, "custo_kwh": 0.47},
        {"solucao_id": 2, "fornecedor_id": 9, "estado_id": 20, "custo_kwh": 0.44},
        {"solucao_id": 1, "fornecedor_id": 10, "estado_id": 20, "custo_kwh": 0.50},
        
        # Estado 21 (RJ) - tarifa: 0.70
        {"solucao_id": 1, "fornecedor_id": 1, "estado_id": 21, "custo_kwh": 0.56},
        {"solucao_id": 2, "fornecedor_id": 2, "estado_id": 21, "custo_kwh": 0.53},
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 21, "custo_kwh": 0.59},
        
        # Estado 22 (RO) - tarifa: 0.49
        {"solucao_id": 1, "fornecedor_id": 4, "estado_id": 22, "custo_kwh": 0.39},
        {"solucao_id": 2, "fornecedor_id": 5, "estado_id": 22, "custo_kwh": 0.37},
        {"solucao_id": 1, "fornecedor_id": 6, "estado_id": 22, "custo_kwh": 0.42},
        
        # Estado 23 (RR) - tarifa: 0.54
        {"solucao_id": 1, "fornecedor_id": 7, "estado_id": 23, "custo_kwh": 0.43},
        {"solucao_id": 2, "fornecedor_id": 8, "estado_id": 23, "custo_kwh": 0.41},
        {"solucao_id": 1, "fornecedor_id": 9, "estado_id": 23, "custo_kwh": 0.46},
        
        # Estado 24 (SC) - tarifa: 0.83
        {"solucao_id": 1, "fornecedor_id": 10, "estado_id": 24, "custo_kwh": 0.66},
        {"solucao_id": 2, "fornecedor_id": 1, "estado_id": 24, "custo_kwh": 0.62},
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 24, "custo_kwh": 0.70},
        
        # Estado 25 (SE) - tarifa: 0.78
        {"solucao_id": 1, "fornecedor_id": 3, "estado_id": 25, "custo_kwh": 0.62},
        {"solucao_id": 2, "fornecedor_id": 4, "estado_id": 25, "custo_kwh": 0.59},
        {"solucao_id": 1, "fornecedor_id": 5, "estado_id": 25, "custo_kwh": 0.66},
        
        # Estado 26 (SP) - tarifa: 0.85
        {"solucao_id": 1, "fornecedor_id": 6, "estado_id": 26, "custo_kwh": 0.68},
        {"solucao_id": 2, "fornecedor_id": 7, "estado_id": 26, "custo_kwh": 0.64},
        {"solucao_id": 1, "fornecedor_id": 8, "estado_id": 26, "custo_kwh": 0.72},
        {"solucao_id": 2, "fornecedor_id": 9, "estado_id": 26, "custo_kwh": 0.68},
        
        # Estado 27 (TO) - tarifa: 0.97
        {"solucao_id": 1, "fornecedor_id": 10, "estado_id": 27, "custo_kwh": 0.78},
        {"solucao_id": 2, "fornecedor_id": 1, "estado_id": 27, "custo_kwh": 0.73},
        {"solucao_id": 1, "fornecedor_id": 2, "estado_id": 27, "custo_kwh": 0.82},
        {"solucao_id": 2, "fornecedor_id": 3, "estado_id": 27, "custo_kwh": 0.77},
    ]

    for sf in solucao_fornecedores:
        existe = SolucaoFornecedor.query.filter_by(solucao_id=sf["solucao_id"], fornecedor_id=sf["fornecedor_id"], estado_id=sf["estado_id"]).first()
        if not existe:
            nova_solucao_fornecedor = SolucaoFornecedor(**sf)
            db.session.add(nova_solucao_fornecedor)
    
    db.session.commit()
    print("sucesso: soluções fornecedores inseridos")