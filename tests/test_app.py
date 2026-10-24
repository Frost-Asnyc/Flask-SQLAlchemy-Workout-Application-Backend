from workout_api import create_app
from workout_api.extensions import db
from workout_api.models import Exercise, Workout, WorkoutExercise


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def test_health_check():
    client = create_app(TestConfig).test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_workout_exercise_relationships():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        workout = Workout()
        exercise = Exercise(name="Squat")
        workout_exercise = WorkoutExercise(
            workout=workout,
            exercise=exercise,
            reps=10,
            sets=3,
        )

        db.session.add(workout_exercise)
        db.session.commit()

        assert workout.workout_exercises == [workout_exercise]
        assert exercise.workout_exercises == [workout_exercise]
        assert workout_exercise.workout is workout
        assert workout_exercise.exercise is exercise
