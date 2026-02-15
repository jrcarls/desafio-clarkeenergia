# backend/tests/test_routes/test_estados.py
def test_listar_estados(client, estado_teste):
    """Testa listagem de estados"""
    response = client.get('/api/v1/estados')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['nome'] == 'São Paulo'

def test_listar_estados_vazio(client):
    """Testa listagem vazia"""
    response = client.get('/api/v1/estados')
    assert response.status_code == 200
    assert response.get_json() == []