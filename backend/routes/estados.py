from flask import Blueprint

bp_estados = Blueprint('estados', __name__)

@bp_estados.route("/api/v1/estados", methods=['GET'])
def estados():
    return "<p>Estados API</p>"
