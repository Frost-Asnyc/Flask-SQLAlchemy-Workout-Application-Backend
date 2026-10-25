from marshmallow import Schema, fields, validate


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(allow_none=True, validate=validate.Range(min=1))
    sets = fields.Int(allow_none=True, validate=validate.Range(min=1))
    duration_seconds = fields.Int(
        allow_none=True, validate=validate.Range(min=0)
    )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=0))
    notes = fields.Str(allow_none=True, validate=validate.Length(max=1000))
    workout_exercises = fields.List(
        fields.Nested(WorkoutExerciseSchema), dump_only=True
    )
