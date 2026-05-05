# Aerospace & Defense Resource Management Application

**Generated**: May 5, 2026  
**Domain**: Aerospace & Defense  
**Version**: 0.0.1

## Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Frontend** | Angular | 21.2.11 |
| **Backend** | Python Flask | 3.0.0 |
| **Database** | PostgreSQL | 15 |
| **ORM** | SQLAlchemy | 2.0.27 |
| **Cloud** | AWS (S3, RDS, EC2) | Latest SDK |
| **Authentication** | JWT | - |
| **Package Manager** | npm | - |

## Project Structure

```
aerospace-and-defense-verify-clean-restart-submodule-and-bra/
├── src/                          # Angular Frontend
│   ├── app.component.*           # Root component
│   ├── index.html                # HTML entry
│   ├── main.ts                   # Angular bootstrap
│   ├── styles.scss               # Global styles
│   └── assets/                   # Static assets
├── backend/                      # Python Backend
│   ├── app/
│   │   ├── models/               # Database models
│   │   ├── routes/               # API endpoints
│   │   ├── services/             # Business logic & AWS
│   │   └── utils/                # Helpers
│   ├── run.py                    # Flask entry point
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # Backend documentation
├── specs/                        # Specification documents
│   └── 1-general-requirements-business-user/
│       ├── spec.md               # Feature specification
│       ├── plan.md               # Implementation plan
│       ├── tasks.md              # Story tasks
│       └── ...
├── angular.json                  # Angular configuration
├── tsconfig.json                 # TypeScript configuration
├── package.json                  # npm dependencies
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
└── README.md                     # This file
```

## Quick Start

### Prerequisites
- **Node.js** v25.x
- **npm** 10.x
- **Python** 3.11+
- **PostgreSQL** 15
- **Git**

### Installation

1. **Clone and navigate to the submodule**
```bash
cd aerospace-and-defense-verify-clean-restart-submodule-and-bra
```

2. **Install Frontend Dependencies**
```bash
npm install --legacy-peer-deps
```

3. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Initialize Database** (if PostgreSQL is running)
```bash
python -c "from backend.app import create_app, db; app = create_app(); \
app.app_context().push(); db.create_all()"
```

### Development

**Start both servers (Frontend + Backend):**
```bash
npm run dev
```

**Or start individually:**
```bash
# Terminal 1 - Frontend (Angular)
npm run dev:frontend
# Runs on http://localhost:4201

# Terminal 2 - Backend (Flask)
npm run dev:backend
# Runs on http://localhost:8000
```

### Building for Production

```bash
npm run build
```
Output: `dist/aerospace-and-defense/`

## API Documentation

### Base URL
```
http://localhost:8000/api
```

### Health Check
```http
GET /health/
```

### Requirements Endpoints

**List Requirements**
```http
GET /requirements/
```

**Create Requirement**
```http
POST /requirements/
Content-Type: application/json

{
  "title": "General Requirements",
  "description": "...",
  "creator": "User",
  "producer": "Producer",
  "status": "draft",
  "priority": "high"
}
```

**Get Requirement**
```http
GET /requirements/{id}
```

**Get User Stories for Requirement**
```http
GET /requirements/{id}/user-stories
```

**Create User Story**
```http
POST /requirements/{id}/user-stories
Content-Type: application/json

{
  "title": "Story Title",
  "description": "...",
  "acceptance_criteria": "...",
  "status": "draft",
  "priority": "high",
  "estimated_effort": 8
}
```

## Database Schema

### Requirements Table
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | Primary Key |
| creation_date | DateTime | Timestamp |
| modification_date | DateTime | Timestamp |
| creator | String | User identifier |
| producer | String | System/user identifier |
| title | String | Requirement title |
| description | Text | Full description |
| status | String | draft, approved, implemented |
| priority | String | high, medium, low |
| created_at | DateTime | Record creation |
| updated_at | DateTime | Record modification |

### UserStories Table
| Column | Type | Notes |
|--------|------|-------|
| id | UUID | Primary Key |
| requirement_id | UUID | Foreign Key to Requirements |
| title | String | Story title |
| description | Text | Story description |
| acceptance_criteria | Text | Definition of done |
| status | String | draft, in_progress, done |
| priority | String | high, medium, low |
| estimated_effort | Integer | Story points |
| created_at | DateTime | Record creation |
| updated_at | DateTime | Record modification |

## AWS Integration

The backend is configured to integrate with AWS services:

### S3 (Object Storage)
- Document upload/download
- File management for requirements

### RDS (Relational Database)
- PostgreSQL instance management
- Automated backups and snapshots

### EC2 (Compute Instances)
- Application deployment
- Infrastructure monitoring

**Configuration**:
Set AWS credentials in `.env`:
```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_S3_BUCKET=aerospace-defense-bucket
```

## Features

✅ **Frontend (Angular)**
- Interactive UI with Bootstrap styling
- Real-time updates (Hot Module Reloading)
- Responsive design
- TypeScript strict mode

✅ **Backend (Flask)**
- RESTful API design
- CORS support
- PostgreSQL integration
- AWS SDK integration
- Request validation
- Error handling

✅ **Development**
- Concurrent frontend + backend startup
- Environment variable support
- Database ORM with migrations
- Logging and monitoring

## Specification and Tasks

### Feature: General Requirements (Business User)
**Story ID**: US-1

Review the specification documents:
- **Specification**: [specs/1-general-requirements-business-user/spec.md](specs/1-general-requirements-business-user/spec.md)
- **Implementation Plan**: [specs/1-general-requirements-business-user/plan.md](specs/1-general-requirements-business-user/plan.md)
- **Story Tasks**: [specs/1-general-requirements-business-user/tasks.md](specs/1-general-requirements-business-user/tasks.md)

### Task Count
- **Total Tasks**: 29+
- **Categories**: Design, Implementation, Testing, Documentation

## Development Workflow

1. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make Changes**
   - Frontend: Edit components in `src/`
   - Backend: Edit Flask routes in `backend/app/routes/`

3. **Run Tests**
```bash
# Frontend
ng test

# Backend
pytest backend/
```

4. **Commit Changes**
```bash
git add .
git commit -m "feat: description of changes"
git push origin feature/your-feature-name
```

5. **Create Pull Request**
   - Base branch: `develop`
   - Ensure CI/CD checks pass

## Environment Variables

See `.env.example` for all available configuration options:

```env
# Flask
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/aerospace_db

# AWS
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...

# CORS
CORS_ORIGINS=http://localhost:4201,http://localhost:4200
```

## Troubleshooting

### Port Already in Use
```bash
# Find process on port 8000
lsof -i :8000
# Kill process
kill -9 <PID>
```

### Database Connection Error
```bash
# Verify PostgreSQL is running
psql --version
# Check connection string in .env
```

### Angular Module Not Found
```bash
# Clear npm cache and reinstall
npm cache clean --force
npm install --legacy-peer-deps
```

## Resources

- [Angular Documentation](https://angular.io/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Guide](https://docs.sqlalchemy.org/)
- [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

## Git Strategy

- **Parent Branch**: `006-research-data-management`
- **Child Branch**: `develop` (default for submodule)
- **Feature Branches**: `feature/*` from `develop`
- **Pull Request Target**: `develop`

## Contact & Support

For issues or questions:
1. Review specification documents
2. Check troubleshooting section
3. Review implementation notes in `specs/`

---

**Generated from Speckit Workflow** - Aerospace & Defense Resource Management System  
**Branch**: develop | **Version**: 0.0.1
