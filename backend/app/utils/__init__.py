"""Utility functions"""
import logging
from functools import wraps
from flask import jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_errors(f):
    """Decorator to handle common errors"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 400
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
    return decorated_function


def validate_request(required_fields):
    """Decorator to validate required fields in request"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from flask import request
            data = request.get_json() or {}
            missing = [field for field in required_fields if field not in data]
            if missing:
                return jsonify({'status': 'error', 'message': f'Missing required fields: {missing}'}), 400
            return f(*args, **kwargs)
        return decorated_function
    return decorator
