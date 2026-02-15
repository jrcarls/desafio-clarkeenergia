# backend/tests/conftest.py
import pytest
from app import create_app, db
from models.estado import Estado
from models.fornecedor import Fornecedor
from models.solucao import Solucao
from models.solucao_fornecedor import SolucaoFornecedor

@pytest.fixture
def app():
    """Cria uma app Flask de teste"""
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Cliente HTTP para testes"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """CLI runner para testes"""
    return app.test_cli_runner()

@pytest.fixture
def app_context(app):
    """Contexto da aplicação"""
    with app.app_context():
        yield app

# Fixtures de dados
@pytest.fixture
def estado_teste(app_context):
    """Cria um estado para testes"""
    estado = Estado(
        nome='São Paulo',
        sigla='SP',
        tarifa_base_kwh=0.75
    )
    db.session.add(estado)
    db.session.commit()
    return estado

@pytest.fixture
def fornecedor_teste(app_context, estado_teste):
    """Cria um fornecedor para testes"""
    fornecedor = Fornecedor(
        nome='Fornecedor Teste',
        logo='logo.png',
        estado_origem_id=estado_teste.id,  # Corrigido: estado_origem_id não estado_id
        total_clientes=1000,
        avaliacoes_media=4.5
    )
    db.session.add(fornecedor)
    db.session.commit()
    return fornecedor

@pytest.fixture
def solucao_teste(app_context):
    """Cria uma solução para testes"""
    solucao = Solucao(
        cod='SOL001',
        nome='Solar'
    )
    db.session.add(solucao)
    db.session.commit()
    return solucao

@pytest.fixture
def solucao_fornecedor_teste(app_context, estado_teste, fornecedor_teste, solucao_teste):
    """Cria uma relação solução-fornecedor"""
    sf = SolucaoFornecedor(
        estado_id=estado_teste.id,
        fornecedor_id=fornecedor_teste.id,
        solucao_id=solucao_teste.id,
        custo_kwh=0.50
    )
    db.session.add(sf)
    db.session.commit()
    return sf