from flask import Blueprint, request
from schemas.solucao_fornecedor import SolucaoFornecedor as SolucaoFornecedorSchema
from services.simulador_service import simular_economia

bp_simulador = Blueprint("simulador", __name__)
@bp_simulador.route("/api/v1/simulador", methods=["POST"])
def simular():
    data = request.get_json()
    estado_id = data.get("estado_id")
    consumo_kwh = data.get("consumo_kwh")

    resultado = simular_economia(estado_id, consumo_kwh)

    schema = SolucaoFornecedorSchema(many=True)
    resultado_serializado = schema.dump(resultado)

    return resultado_serializado, 200