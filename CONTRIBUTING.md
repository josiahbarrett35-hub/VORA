# Contributing to VORA

## Development Setup

### Prerequisites
- Docker Desktop
- Git
- Python 3.11+ (for local backend work)
- Node 18+ (for local frontend work)

### Quick Start
- git clone https://github.com/josiaharrett35-hub/VORA.git
- cd VORA
- docker-compose up -d


### Services
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## Code Standards

- Backend: Black (formatting), Flake8 (linting)
- Frontend: ESLint, Prettier
- Both: Type hints/TypeScript

## Git Workflow

1. Create feature branch: `git checkout -b feature/your-feature`
2. Commit frequently with clear messages
3. Push: `git push origin feature/your-feature`
4. Create Pull Request
5. After merge, delete branch: `git push origin --delete feature/your-feature`
