"""README for Backend Setup"""
# Aerospace & Defense Backend API

## Tech Stack
- **Framework**: Flask 3.0.0
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT
- **Cloud**: AWS SDK (S3, RDS, EC2)

## Project Structure
```
backend/
├── app/
│   ├── __init__.py       # Flask app factory
│   ├── models/           # Database models
│   ├── routes/           # API blueprints
│   ├── services/         # AWS and business logic
│   └── utils/            # Helper functions
├── run.py                # Entry point
├── requirements.txt      # Python dependencies
└── README.md
```

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Initialize Database
```bash
# Ensure PostgreSQL is running
python -c "from app import create_app; app = create_app(); app.app_context().push()"
```

### 4. Run the Application
```bash
python backend/run.py
```
Server will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /api/health/` - Application health status

### Requirements
- `GET /api/requirements/` - List all requirements
- `POST /api/requirements/` - Create requirement
- `GET /api/requirements/<id>` - Get requirement details
- `GET /api/requirements/<id>/user-stories` - Get user stories
- `POST /api/requirements/<id>/user-stories` - Create user story

## Database Models

### Requirement
- ID (UUID)
- Title
- Description
- Creation Date
- Modification Date
- Creator
- Producer
- Status
- Priority

### UserStory
- ID (UUID)
- Requirement ID (Foreign Key)
- Title
- Description
- Acceptance Criteria
- Status
- Priority
- Estimated Effort

## AWS Integration
The application includes AWS SDK integration for:
- **S3**: File storage and document management
- **RDS**: Database management and backups
- **EC2**: Instance management for deployment

Configure AWS credentials in `.env` or use IAM roles for EC2 deployment.
