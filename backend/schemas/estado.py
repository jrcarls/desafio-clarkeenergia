from marshmallow import Schema, fields

class Estado(Schema):
    id = fields.Int()
    nome = fields.Str()
    sigla = fields.Str()
    tarifa_base_kwh = fields.Float()
