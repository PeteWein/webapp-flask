from flask import Flask

def create_app():
    """Initialize the core application factory."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    # Initialize Plugins Here

    with app.app_context():
        
        # Include our Routes
        from . import routes

        # Register Blueprints
        # currently none

        return app
