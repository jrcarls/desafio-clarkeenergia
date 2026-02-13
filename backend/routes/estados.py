from flask import Blueprint, jsonify
from model.estado import Estado
from schemas.estado import Estado as EstadoSchema

bp_estados = Blueprint("estados", __name__)

@bp_estados.route("/api/v1/estados", methods=["GET"])
def listar_estados():
    estados = Estado.query.all()

    schema = EstadoSchema(many=True)
    resultado = schema.dump(estados)

    return jsonify(resultado), 200
