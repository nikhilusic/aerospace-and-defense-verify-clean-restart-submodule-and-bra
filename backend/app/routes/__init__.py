"""API Routes"""
from flask import Blueprint, jsonify, request
from app import db
from app.models import Requirement, UserStory

# Health check blueprint
health_bp = Blueprint('health', __name__, url_prefix='/api/health')

@health_bp.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Aerospace & Defense API is running',
        'version': '0.0.1'
    }), 200


# Requirements blueprint
requirements_bp = Blueprint('requirements', __name__, url_prefix='/api/requirements')

@requirements_bp.route('/', methods=['GET'])
def get_requirements():
    """Get all requirements"""
    try:
        requirements = Requirement.query.all()
        return jsonify({
            'status': 'success',
            'data': [req.to_dict() for req in requirements],
            'count': len(requirements)
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@requirements_bp.route('/', methods=['POST'])
def create_requirement():
    """Create a new requirement"""
    try:
        data = request.get_json()
        requirement = Requirement(
            title=data.get('title'),
            description=data.get('description'),
            creator=data.get('creator'),
            producer=data.get('producer'),
            status=data.get('status', 'draft'),
            priority=data.get('priority')
        )
        db.session.add(requirement)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'data': requirement.to_dict(),
            'message': 'Requirement created successfully'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500


@requirements_bp.route('/<requirement_id>', methods=['GET'])
def get_requirement(requirement_id):
    """Get a specific requirement by ID"""
    try:
        requirement = Requirement.query.get(requirement_id)
        if not requirement:
            return jsonify({'status': 'error', 'message': 'Requirement not found'}), 404
        
        return jsonify({
            'status': 'success',
            'data': requirement.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@requirements_bp.route('/<requirement_id>/user-stories', methods=['GET'])
def get_requirement_stories(requirement_id):
    """Get user stories for a requirement"""
    try:
        stories = UserStory.query.filter_by(requirement_id=requirement_id).all()
        return jsonify({
            'status': 'success',
            'data': [story.to_dict() for story in stories],
            'count': len(stories)
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@requirements_bp.route('/<requirement_id>/user-stories', methods=['POST'])
def create_user_story(requirement_id):
    """Create a user story for a requirement"""
    try:
        # Verify requirement exists
        requirement = Requirement.query.get(requirement_id)
        if not requirement:
            return jsonify({'status': 'error', 'message': 'Requirement not found'}), 404
        
        data = request.get_json()
        story = UserStory(
            requirement_id=requirement_id,
            title=data.get('title'),
            description=data.get('description'),
            acceptance_criteria=data.get('acceptance_criteria'),
            status=data.get('status', 'draft'),
            priority=data.get('priority'),
            estimated_effort=data.get('estimated_effort')
        )
        db.session.add(story)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'data': story.to_dict(),
            'message': 'User story created successfully'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
