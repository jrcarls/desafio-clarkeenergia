from flask import Blueprint, jsonify
from model.estado import Estado

bp_estados = Blueprint('estados', __name__)

@bp_estados.route("/api/v1/estados", methods=['GET'])
def estados():
    estados = Estado.query.all()
    estados_list = [
        {
            "id": e.id,
            "nome": e.nome,
            "sigla": e.sigla,
            "tarifa_base_kwh": e.tarifa_base_kwh
        } for e in estados
    ]
    
    return jsonify(estados_list)
