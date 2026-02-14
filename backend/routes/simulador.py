from flask import Blueprint, jsonify, request


bp_simulador = Blueprint("simulador", __name__)
@bp_simulador.route("/api/v1/simulador", methods=["POST"])
def simular():
    data = request.get_json()
    estado_id = data.get("estado_id")
    consumo_kwh = data.get("consumo_kwh")


    # mock substituir pela funcao  de calculo simulador_service
    resultado = {
        "estado_id": estado_id,
        "consumo_kwh": consumo_kwh,
        "custo_total": 100.0
    }

    return jsonify(resultado), 200