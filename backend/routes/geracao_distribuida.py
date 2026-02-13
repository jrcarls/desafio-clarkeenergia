from flask import Blueprint

bp_geracao_distribuida = Blueprint('geracao_distribuida', __name__)

@bp_geracao_distribuida.route("/geracao_distribuida")
def hello_world():
    return "<p>Geração distribuida</p>"
