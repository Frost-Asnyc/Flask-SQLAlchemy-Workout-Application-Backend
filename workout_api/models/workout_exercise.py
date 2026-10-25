from workout_api.extensions import db


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(
        db.Integer, db.ForeignKey("workouts.id"), nullable=False
    )
    exercise_id = db.Column(
        db.Integer, db.ForeignKey("exercises.id"), nullable=False
    )
    reps = db.Column(db.Integer, nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True)

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    __table_args__ = (
        db.CheckConstraint("reps IS NULL OR reps >= 1", name="ck_workout_exercise_reps"),
        db.CheckConstraint("sets IS NULL OR sets >= 1", name="ck_workout_exercise_sets"),
        db.CheckConstraint(
            "duration_seconds IS NULL OR duration_seconds >= 0",
            name="ck_workout_exercise_duration_seconds",
        ),
        db.UniqueConstraint("workout_id", "exercise_id", name="uq_workout_exercise"),
    )

    def __repr__(self):
        return f"<WorkoutExercise {self.id}: workout={self.workout_id}, exercise={self.exercise_id}>"
