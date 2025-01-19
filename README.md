# PostgreSQL Microservice

A robust, production-ready RESTful microservice built with FastAPI and PostgreSQL, following clean architecture principles and best practices.

## 🚀 Features

- **FastAPI Backend**: High-performance REST API
- **PostgreSQL Database**: Reliable data storage
- **SQLAlchemy ORM**: Efficient database operations
- **Clean Architecture**: Maintainable and scalable code structure
- **Docker Support**: Easy deployment and scaling
- **API Documentation**: Auto-generated OpenAPI/Swagger docs
- **Type Checking**: Full type hints throughout
- **Automated Tests**: Comprehensive test suite
- **API Versioning**: Support for multiple API versions

## 🏗️ Project Structure

```
.
├── app/
│   ├── api/              # API endpoints
│   │   ├── deps.py      # Dependencies (e.g., DB sessions)
│   │   └── v1/          # API version 1
│   ├── core/            # Core modules
│   │   ├── config.py    # Configuration
│   │   └── logging.py   # Logging setup
│   ├── db/              # Database
│   │   ├── base.py      # Base class
│   │   └── session.py   # DB session
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic models
│   ├── services/        # Business logic
│   └── main.py         # FastAPI application
├── tests/              # Test suite
├── scripts/            # Utility scripts
├── requirements/       # Dependencies
├── Dockerfile         # Docker configuration
└── docker-compose.yml # Docker Compose config
```

## 🛠️ Prerequisites

- Docker and Docker Compose
- Python 3.11+
- PostgreSQL 15+

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd postgres-microservice
   ```

2. **Environment Setup**
   ```bash
   # Create a virtual environment
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements/dev.txt
   ```

4. **Run with Docker**
   ```bash
   docker-compose up --build
   
   or 
   
   docker compose up --build

   ```

5. **Access the API**
   - API: http://localhost:8000/api/v1
   - Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## 🔧 Development

### Local Development Setup

1. **Install development dependencies**
   ```bash
   pip install -r requirements/dev.txt
   ```

2. **Run tests**
   ```bash
   pytest
   ```

3. **Code formatting**
   ```bash
   # Format code
   black .
   
   # Sort imports
   isort .
   
   # Lint code
   flake8
   ```

### Database Migrations

```bash
# Generate migration
alembic revision --autogenerate -m "description"

# Run migrations
alembic upgrade head
```

## 📚 API Documentation

### Endpoints

#### Items API
- `GET /api/v1/items/`: List all items
- `POST /api/v1/items/`: Create new item
- `GET /api/v1/items/{id}`: Get item details
- `PUT /api/v1/items/{id}`: Update item
- `DELETE /api/v1/items/{id}`: Delete item

### Example Requests

```bash
# Create item
curl -X POST "http://localhost:8000/api/v1/items/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Item", "description": "Description"}'

# Get items
curl "http://localhost:8000/api/v1/items/"
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/api/v1/test_items.py
```

## 🔒 Environment Variables

Required environment variables:
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `POSTGRES_HOST`: Database host
- `POSTGRES_PORT`: Database port

## 🚀 Deployment

### Docker Deployment
```bash
# Build and run services
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Considerations
- Set secure database credentials
- Configure proper logging
- Set up monitoring
- Implement rate limiting
- Add authentication/authorization
- Configure CORS properly
- Set up proper backup strategy

## 📈 Monitoring

- Database health checks are configured
- Application metrics available at `/metrics`
- Logs available via Docker logs

## 🔑 Security

- Input validation using Pydantic
- SQL injection protection via SQLAlchemy
- Proper error handling
- Environment-based configurations
- Containerized services

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker