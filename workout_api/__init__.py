from flask import Flask

from workout_api.extensions import db, migrate


def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("workout_api.config.Config")
    if config_object is not None:
        app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)

    from workout_api.routes import api

    app.register_blueprint(api)
    return app
