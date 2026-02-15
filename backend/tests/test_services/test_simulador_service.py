# backend/tests/test_services/test_simulador_service.py
import pytest
from app import db
from models.fornecedor import Fornecedor
from models.solucao import Solucao
from models.solucao_fornecedor import SolucaoFornecedor
from services.simulador_service import simular_economia

def test_simular_economia_calculo(app_context, solucao_fornecedor_teste, estado_teste):
    """Testa cálculo da economia"""
    resultado = simular_economia(estado_teste.id, 200)
    assert isinstance(resultado, list)
    assert len(resultado) == 1
    assert resultado[0]['economia'] == 50.0  # (200*0.75) - (200*0.50) = 150 - 100 = 50

def test_simular_economia_percentual(app_context, solucao_fornecedor_teste, estado_teste):
    """Testa cálculo da economia percentual"""
    resultado = simular_economia(estado_teste.id, 200)
    esperado = (50.0 / 150.0) * 100
    assert abs(resultado[0]['economia_percentual'] - esperado) < 0.01

def test_simular_economia_multiplos_fornecedores(app_context, estado_teste):
    """Testa simulação com múltiplos fornecedores"""
    
    solucao = Solucao(cod='SOL002', nome='Eólica')
    db.session.add(solucao)
    db.session.commit()
    
    for i in range(3):
        fornecedor = Fornecedor(
            nome=f'Fornecedor {i}',
            logo=f'logo{i}.png',
            estado_origem_id=estado_teste.id,  # Corrigido: estado_origem_id não estado_id
            total_clientes=1000,
            avaliacoes_media=4.0
        )
        db.session.add(fornecedor)
        db.session.commit()
        
        sf = SolucaoFornecedor(
            estado_id=estado_teste.id,
            fornecedor_id=fornecedor.id,
            solucao_id=solucao.id,
            custo_kwh=0.40 + i*0.05
        )
        db.session.add(sf)
    db.session.commit()
    
    resultado = simular_economia(estado_teste.id, 100)
    assert len(resultado) == 3