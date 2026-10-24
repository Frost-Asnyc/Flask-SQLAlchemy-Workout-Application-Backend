from flask import Blueprint, jsonify, request

from workout_api.extensions import db
from workout_api.models import Exercise, Workout, WorkoutExercise
from workout_api.schemas import ExerciseSchema, WorkoutExerciseSchema, WorkoutSchema

api = Blueprint("api", __name__)

exercise_schema = ExerciseSchema()
exercise_list_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workout_list_schema = WorkoutSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()


@api.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@api.get("/exercises")
@api.get("/api/exercises")
def get_exercises():
    exercises = Exercise.query.order_by(Exercise.id).all()
    return jsonify(exercise_list_schema.dump(exercises)), 200


@api.post("/exercises")
@api.post("/api/exercises")
def create_exercise():
    payload = request.get_json(silent=True) or {}
    errors = exercise_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    exercise = Exercise(**exercise_schema.load(payload))
    db.session.add(exercise)
    db.session.commit()
    return jsonify(exercise_schema.dump(exercise)), 201


@api.get("/exercises/<int:exercise_id>")
@api.get("/api/exercises/<int:exercise_id>")
def get_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    return jsonify(exercise_schema.dump(exercise)), 200


@api.put("/exercises/<int:exercise_id>")
@api.put("/api/exercises/<int:exercise_id>")
def update_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    payload = request.get_json(silent=True) or {}
    errors = exercise_schema.validate(payload, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400

    for key, value in exercise_schema.load(payload, partial=True).items():
        setattr(exercise, key, value)

    db.session.commit()
    return jsonify(exercise_schema.dump(exercise)), 200


@api.delete("/exercises/<int:exercise_id>")
@api.delete("/api/exercises/<int:exercise_id>")
def delete_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message": "Exercise deleted"}), 200


@api.get("/workouts")
@api.get("/api/workouts")
def get_workouts():
    workouts = Workout.query.order_by(Workout.id).all()
    return jsonify(workout_list_schema.dump(workouts)), 200


@api.post("/workouts")
@api.post("/api/workouts")
def create_workout():
    payload = request.get_json(silent=True) or {}
    errors = workout_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    workout = Workout(**workout_schema.load(payload))
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout_schema.dump(workout)), 201


@api.get("/workouts/<int:workout_id>")
@api.get("/api/workouts/<int:workout_id>")
def get_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    return jsonify(workout_schema.dump(workout)), 200


@api.put("/workouts/<int:workout_id>")
@api.put("/api/workouts/<int:workout_id>")
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    payload = request.get_json(silent=True) or {}
    errors = workout_schema.validate(payload, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400

    for key, value in workout_schema.load(payload, partial=True).items():
        setattr(workout, key, value)

    db.session.commit()
    return jsonify(workout_schema.dump(workout)), 200


@api.delete("/workouts/<int:workout_id>")
@api.delete("/api/workouts/<int:workout_id>")
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout deleted"}), 200


@api.get("/workouts/<int:workout_id>/exercises")
@api.get("/api/workouts/<int:workout_id>/exercises")
def get_workout_exercises(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    return jsonify(
        [workout_exercise_schema.dump(item) for item in workout.workout_exercises]
    ), 200


@api.post("/workouts/<int:workout_id>/exercises")
@api.post("/api/workouts/<int:workout_id>/exercises")
def add_workout_exercise(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    payload = request.get_json(silent=True) or {}
    errors = workout_exercise_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    exercise_id = payload["exercise_id"]
    exercise = Exercise.query.get_or_404(exercise_id)
    workout_exercise = WorkoutExercise(
        workout=workout,
        exercise=exercise,
        reps=payload.get("reps"),
        sets=payload.get("sets"),
        duration_seconds=payload.get("duration_seconds"),
    )
    db.session.add(workout_exercise)
    db.session.commit()
    return jsonify(workout_exercise_schema.dump(workout_exercise)), 201
