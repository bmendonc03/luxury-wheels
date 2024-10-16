from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o SQLAlchemy para o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luxury_wheels.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)

    # Importa e registra os blueprints (rotas)
    from .routes import api
    app.register_blueprint(api)

    return app
