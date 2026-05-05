"""Flask Application Factory"""
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()


def create_app(config_name=None):
    """Application factory function"""
    app = Flask(__name__)

    raw_db_url = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/aerospace_db')
    if raw_db_url.startswith('postgresql://'):
        host_part = raw_db_url.split('://', 1)[1].split('/', 1)[0]
        if '@' not in host_part:
            db_user = os.getenv('PGUSER') or os.getenv('USER') or 'postgres'
            raw_db_url = raw_db_url.replace('postgresql://', f'postgresql+pg8000://{db_user}@', 1)
        else:
            raw_db_url = raw_db_url.replace('postgresql://', 'postgresql+pg8000://', 1)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = raw_db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Initialize extensions
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": os.getenv('CORS_ORIGINS', 'http://localhost:4201').split(',')}})
    
    # Register blueprints
    from app.routes import health_bp, requirements_bp
    app.register_blueprint(health_bp)
    app.register_blueprint(requirements_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
