from flask import Flask

app = None

def create_app():
    global app
    if app is None:
        app = Flask(__name__)
        with app.app_context():
            from app import routes  # Import routes here to avoid circular imports
    return app
