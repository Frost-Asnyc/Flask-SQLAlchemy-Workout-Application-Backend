from workout_api.extensions import db


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="workout"
    )
