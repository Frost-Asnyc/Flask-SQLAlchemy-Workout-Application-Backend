# Flask SQLAlchemy Workout Application Backend

Owned and maintained by: Lerionka Olentiki

A Flask REST API backend for a workout-tracking application. The project supports reusable exercises, workouts, and workout-specific exercise entries with metadata such as sets, reps, and duration.

## Features

- Exercise CRUD endpoints
- Workout CRUD endpoints
- Workout-to-exercise relationship management
- Marshmallow validation for request payloads
- SQLAlchemy model relationships with database constraints
- Automated tests for health check and relationship behavior

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

The application starts a Flask API and exposes a healing endpoint at `GET /health`.

## API endpoints

### Health

- `GET /health`
- `GET /api/health`

### Exercises

- `GET /exercises`
- `POST /exercises`
- `GET /exercises/<exercise_id>`
- `PUT /exercises/<exercise_id>`
- `DELETE /exercises/<exercise_id>`

### Workouts

- `GET /workouts`
- `POST /workouts`
- `GET /workouts/<workout_id>`
- `PUT /workouts/<workout_id>`
- `DELETE /workouts/<workout_id>`

### Workout exercises

- `GET /workouts/<workout_id>/exercises`
- `POST /workouts/<workout_id>/exercises`

## Project structure

```text
workout_api/
  __init__.py        Flask app factory
  config.py          Application configuration
  extensions.py      Database and migration setup
  models/            SQLAlchemy models
  routes/            API blueprint and endpoint logic
  schemas/           Marshmallow serialization and validation
tests/               Automated tests
run.py               Application entry point
Pipfile              Dependencies and environment config
README.md            Project documentation
```

## Verification

```bash
pipenv run pytest -q
```

This project includes a basic test suite to validate the app health check and model relationships.

## Ownership

This project was created and is claimed by: Lerionka Olentiki