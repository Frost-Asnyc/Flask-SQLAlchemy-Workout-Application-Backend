from workout_api.extensions import db


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    duration_minutes = db.Column(db.Integer, nullable=True, default=0)
    notes = db.Column(db.Text, nullable=True)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Workout {self.id}: {self.date}>"
