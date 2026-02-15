# backend/tests/test_routes/test_simulador.py
def test_simular_economia(client, solucao_fornecedor_teste, estado_teste):
    """Testa simulação de economia"""
    data = {
        "estado_id": estado_teste.id,
        "consumo_kwh": 100
    }
    response = client.post('/api/v1/simulador', json=data)
    assert response.status_code == 200
    result = response.get_json()
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]['nome'] == 'Fornecedor Teste'
    assert result[0]['custo_base'] == 75.0  # 100 * 0.75
    assert result[0]['custo_fornecedor'] == 50.0  # 100 * 0.50

def test_simular_economia_estado_invalido(client):
    """Testa simulação com estado inválido"""
    data = {
        "estado_id": 999,
        "consumo_kwh": 100
    }
    response = client.post('/api/v1/simulador', json=data)
    assert response.status_code == 200
    result = response.get_json()
    assert result.get("erro") == "Estado não encontrado"

def test_simular_economia_zero(client, solucao_fornecedor_teste, estado_teste):
    """Testa simulação com consumo zero"""
    data = {
        "estado_id": estado_teste.id,
        "consumo_kwh": 0
    }
    response = client.post('/api/v1/simulador', json=data)
    assert response.status_code == 200
    result = response.get_json()
    assert result[0]['economia_percentual'] == 0