from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)
    migrate.init_app(app, db)

    from routes.mercado_livre import bp_mercado_livre
    from routes.geracao_distribuida import bp_geracao_distribuida
    
    app.register_blueprint(bp_mercado_livre)
    app.register_blueprint(bp_geracao_distribuida)

    return app