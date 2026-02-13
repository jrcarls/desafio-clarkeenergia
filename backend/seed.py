from app import db
from model.estado import Estado

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
