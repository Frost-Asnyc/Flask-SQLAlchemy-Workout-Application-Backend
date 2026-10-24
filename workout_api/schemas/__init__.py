"""Marshmallow schemas for validating requests and serializing responses."""

from workout_api.schemas.exercise import ExerciseSchema
from workout_api.schemas.workout import WorkoutExerciseSchema, WorkoutSchema

__all__ = ["ExerciseSchema", "WorkoutExerciseSchema", "WorkoutSchema"]

