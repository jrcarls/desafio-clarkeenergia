from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, origins="*")

    from models.estado import Estado
    from models.fornecedor import Fornecedor
    from models.solucao import Solucao
    from models.solucao_fornecedor import SolucaoFornecedor

    from routes.estados import bp_estados
    from routes.simulador import bp_simulador

    app.register_blueprint(bp_estados)
    app.register_blueprint(bp_simulador)

    @app.cli.command("seed-popular")
    def seed_estados_command():
        from seed import seed_estados, seed_fornecedores, seed_solucoes, seed_solucao_fornecedor
        seed_estados()
        seed_fornecedores()
        seed_solucoes()
        seed_solucao_fornecedor()
        
        print("Seed executado com sucesso!")

    @app.route("/")
    def index():
        return "<p>Clarkeenergia</p>"

    return app