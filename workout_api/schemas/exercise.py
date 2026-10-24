from marshmallow import Schema, fields, validate


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    category = fields.Str(allow_none=True)
    equipment_needed = fields.Bool(load_default=False)
