# FastAPI PostgreSQL Microservice

A robust RESTful microservice built with FastAPI and PostgreSQL, following clean architecture principles and best practices.

## Features

- **FastAPI Backend**: High-performance async REST API
- **PostgreSQL Database**: Reliable data storage with SQLAlchemy ORM
- **Docker Support**: Containerized deployment with Docker and Docker Compose
- **Clean Architecture**: Organized project structure with separation of concerns
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation
- **Type Safety**: Full type hints with Pydantic models
- **Database Migrations**: Alembic for database version control
- **Health Checks**: Built-in database connection health monitoring

## Project Structure

```
postgres-microservice/
├── app/
│   ├── api/              # API endpoints
│   │   ├── deps.py      # Dependencies
│   │   └── v1/          # API version 1
│   ├── core/            # Core configurations
│   ├── db/              # Database configurations
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic models
│   └── services/        # Business logic
├── scripts/             # Utility scripts
├── requirements/        # Dependencies
├── Dockerfile          # Docker configuration
└── docker-compose.yml  # Container orchestration
```

## Prerequisites

- Docker and Docker Compose
- Python 3.11+
- PostgreSQL 15+

## Quick Start

1. **Clone the repository**
```bash
git clone <repository-url>
cd postgres-microservice
```

2. **Build and run with Docker**
```bash
docker-compose up --build
```

3. **Access the API**
- Swagger Documentation: http://localhost:8001/docs
- API Base URL: http://localhost:8001/api/v1

## API Endpoints

### Items API
- `GET /api/v1/items/`: List all items
- `POST /api/v1/items/`: Create a new item
- `GET /api/v1/items/{id}`: Get item details
- `PUT /api/v1/items/{id}`: Update item
- `DELETE /api/v1/items/{id}`: Delete item

### Example Requests

Create an item:
```bash
curl -X POST "http://localhost:8001/api/v1/items/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Item", "description": "Test Description"}'
```

Get all items:
```bash
curl "http://localhost:8001/api/v1/items/"
```

## Development

### Local Setup

1. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

2. **Install dependencies**
```bash
pip install -r requirements/dev.txt
```

3. **Run tests**
```bash
pytest
```

### Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:
```bash
alembic upgrade head
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| POSTGRES_USER | Database user | postgres |
| POSTGRES_PASSWORD | Database password | postgres |
| POSTGRES_DB | Database name | microservice_db |
| POSTGRES_HOST | Database host | db |
| POSTGRES_PORT | Database port | 5432 |

## Docker Configuration

The service uses two containers:
- **web**: FastAPI application
- **db**: PostgreSQL database

Ports:
- API: 8001 (host) -> 8000 (container)
- Database: 5434 (host) -> 5432 (container)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Project Roadmap

Future enhancements:
- [ ] Authentication and Authorization
- [ ] Rate Limiting
- [ ] Caching Layer
- [ ] Metrics Collection
- [ ] Comprehensive Test Suite
- [ ] CI/CD Pipeline

## Troubleshooting

Common issues and solutions:

1. **Database Connection Issues**
   - Check if PostgreSQL is running
   - Verify environment variables
   - Check port availability

2. **Port Conflicts**
   - Change ports in docker-compose.yml
   - Check for processes using the ports

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions and support, please open an issue in the repository.