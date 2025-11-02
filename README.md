# Auth API - Hexagonal Architecture

This project is a simple authentication API built with FastAPI, following the Hexagonal Architecture (Ports and Adapters) and using PostgreSQL as the database.

## Features
- User registration and login endpoints
- JWT token generation for authentication
- Password hashing and verification using bcrypt
- Asynchronous database access with SQLAlchemy and asyncpg
- Separation of concerns via hexagonal architecture

## Technologies
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Passlib (bcrypt)
- Python-Jose (JWT)
- Pydantic

## Project Structure

```
app/
	api/
		main.py                # FastAPI app and startup event
		routers/
			auth_router.py       # Authentication endpoints
		schemas/
			auth.py              # Request models (DTOs)
	application/
		ports/
			user_repository.py   # User repository interface
			auth_service.py      # Auth service interface
		use_cases/
			register_user.py     # Register user use case
			login_user.py        # Login user use case
	config/
		settings.py            # App settings and .env loader
	domain/
		models.py              # Domain models (User)
		services.py            # Password service
	infrastructure/
		models.py              # ORM models
		repositories/
			db.py                # Database connection
			user_repository.py   # Postgres user repository implementation
		security/
			jwt_service.py       # JWT token service
```

## Environment Variables

Sensitive data is stored in the `.env` file:

- `DATABASE_URL`: PostgreSQL connection string
- `JWT_SECRET`: Secret key for JWT token signing
- `JWT_EXPIRES_HOURS`: Token expiration in hours

## How to Run

1. Install dependencies:
	 ```bash
	 pip install -r requirements.txt
	 ```
2. Configure your `.env` file with database credentials and JWT secret.
3. Run database migrations (tables are auto-created on startup).
4. Start the API:
	 ```bash
	 uvicorn app.api.main:app --reload
	 ```

## API Endpoints

- `POST /auth/register`: Register a new user
	- Request: `{ "email": "user@example.com", "password": "string" }`
	- Response: `{ "email": "user@example.com" }`

- `POST /auth/login`: Login and get JWT token
	- Request: `{ "email": "user@example.com", "password": "string" }`
	- Response: `{ "token": "<jwt_token>" }`

## Hexagonal Architecture

The code is organized in layers:
- **Domain**: Core business logic and models
- **Application**: Use cases and interfaces (ports)
- **Infrastructure**: Adapters for database, security, and web
- **API**: HTTP endpoints and request schemas