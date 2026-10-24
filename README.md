# Flask SQLAlchemy Workout Application Backend

A Flask REST API backend for a workout-tracking application. The planned
domain supports trainers, workouts, and reusable exercises, with workout
exercise details such as sets, reps, and duration.

## Requirements

- Python 3.8.13 or newer
- Pipenv

## Installation

```bash
pipenv install --dev
```

## Run the application

```bash
pipenv run python run.py
```

The starter application responds to `GET /health` with a JSON status response.

## Project layout

```text
workout_api/
  models/       SQLAlchemy models
  routes/       API blueprints and endpoints
  schemas/      Marshmallow validation and serialization
  config.py     Application configuration
  extensions.py Flask extension instances
tests/          Automated tests
run.py          Application entry point
```

The domain models, migrations, seed data, and workout API endpoints will be
added on top of this application scaffold.