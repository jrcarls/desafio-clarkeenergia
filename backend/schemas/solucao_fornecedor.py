from marshmallow import Schema, fields

class SolucaoFornecedor(Schema):
    nome = fields.Str()
    logo = fields.Str()
    estado_origem = fields.Str()
    tipo_solucao = fields.Str()
    custo_kwh = fields.Float()
    numero_clientes = fields.Int()
    avaliacao_media = fields.Float()
    custo_base = fields.Float()
    custo_fornecedor = fields.Float()
    economia = fields.Float()
    economia_percentual = fields.Float()