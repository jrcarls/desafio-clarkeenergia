from flask import Blueprint, jsonify, request
from services.simulador_service import simular_economia

bp_simulador = Blueprint("simulador", __name__)
@bp_simulador.route("/api/v1/simulador", methods=["POST"])
def simular():
    data = request.get_json()
    estado_id = data.get("estado_id")
    consumo_kwh = data.get("consumo_kwh")

    resultado = simular_economia(estado_id, consumo_kwh)

    return jsonify(resultado), 200