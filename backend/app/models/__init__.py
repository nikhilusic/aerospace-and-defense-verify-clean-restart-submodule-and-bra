"""Database models for Aerospace & Defense application"""
from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Requirement(db.Model):
    """General Requirements model"""
    __tablename__ = 'requirements'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modification_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    creator = db.Column(db.String(255), nullable=True)
    producer = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='draft')
    priority = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'creation_date': self.creation_date.isoformat(),
            'modification_date': self.modification_date.isoformat(),
            'creator': self.creator,
            'producer': self.producer,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
        }


class UserStory(db.Model):
    """User Stories model"""
    __tablename__ = 'user_stories'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    requirement_id = db.Column(UUID(as_uuid=True), db.ForeignKey('requirements.id'), nullable=False)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text, nullable=True)
    acceptance_criteria = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='draft')
    priority = db.Column(db.String(50), nullable=True)
    estimated_effort = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'requirement_id': str(self.requirement_id),
            'title': self.title,
            'description': self.description,
            'acceptance_criteria': self.acceptance_criteria,
            'status': self.status,
            'priority': self.priority,
            'estimated_effort': self.estimated_effort,
        }
