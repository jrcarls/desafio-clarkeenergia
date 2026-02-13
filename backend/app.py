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

    from model.estado import Estado    
    from routes.estados import bp_estados

    app.register_blueprint(bp_estados)

    @app.cli.command("seed-estados")
    def seed_estados_command():
        from seed import seed_estados
        seed_estados()
        print("Seed executado com sucesso!")

    @app.route("/")
    def index():
        return "<p>Clarkeenergia</p>"

    return app