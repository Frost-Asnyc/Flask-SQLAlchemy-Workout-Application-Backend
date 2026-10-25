from workout_api.extensions import db


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    category = db.Column(db.String(120), nullable=True)
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="exercise"
    )

    def __repr__(self):
        return f"<Exercise {self.id}: {self.name}>"
