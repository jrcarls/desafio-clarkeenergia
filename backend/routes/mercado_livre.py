from flask import Blueprint

bp_mercado_livre = Blueprint('mercado_livre', __name__)

@bp_mercado_livre.route("/mercado_livre")
def hello_world():
    return "<p>mercado livre!</p>"
