from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

def create_app():
    from routes import api_blueprint  # Import here to avoid circular import
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app

create_app()

# Ensure the database is created
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
