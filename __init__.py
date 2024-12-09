from flask import Flask
from .config import Config
from .models import db
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load the configurations

    # Initialize the database
    db.init_app(app)

    # Register the blueprint with routes
    app.register_blueprint(bp)

    return app
