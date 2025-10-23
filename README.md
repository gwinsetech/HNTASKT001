# Dynamic Profile Endpoint - Stage 0 Task

A RESTful API built with FastAPI that returns profile information along with dynamic cat facts fetched from an external API.

## 🎯 Features

- **GET /me** - Returns profile information with a fresh cat fact on every request
- **Dynamic Timestamps** - Current UTC time in ISO 8601 format
- **External API Integration** - Fetches cat facts from Cat Facts API
- **Error Handling** - Graceful handling of external API failures
- **CORS Support** - Ready for cross-origin requests
- **Interactive Docs** - Auto-generated API documentation at `/docs`
- **Type Safety** - Full Pydantic validation for requests and responses

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
# Navigate to project directory
cd "C:\Program Files\MS\CORES\HNTASKT001"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Windows CMD:
.\venv\Scripts\activate.bat
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and add your information
# USER_EMAIL=your.email@example.com
# USER_NAME=Your Full Name
# USER_STACK=Python/FastAPI
```

### 4. Run the Application

```bash
# Method 1: Using uvicorn directly
uvicorn main:app --reload

# Method 2: Running the main.py file
python main.py
```

The API will be available at: **http://localhost:8000**

## 📡 API Endpoints

### GET /me

Returns profile information with a dynamic cat fact.

**Response Example:**

```json
{
  "status": "success",
  "user": {
    "email": "john.doe@example.com",
    "name": "John Doe",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-23T12:34:56.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```

### GET /

Root endpoint with API information.

### GET /health

Health check endpoint.

### GET /docs

Interactive API documentation (Swagger UI).

### GET /redoc

Alternative API documentation (ReDoc).

## 🧪 Testing the API

### Using cURL

```bash
curl http://localhost:8000/me
```

### Using PowerShell

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/me" -Method Get
```

### Using Browser

Simply navigate to: http://localhost:8000/me

### Using Interactive Docs

1. Navigate to: http://localhost:8000/docs
2. Click on the `/me` endpoint
3. Click "Try it out"
4. Click "Execute"

## 🏗️ Project Structure

```
HNTASKT001/
├── main.py              # FastAPI application and endpoints
├── models.py            # Pydantic models for type safety
├── config.py            # Configuration and settings
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## ⚙️ Configuration

All configuration is managed through environment variables in the `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `USER_EMAIL` | Your email address | your.email@example.com |
| `USER_NAME` | Your full name | Your Full Name |
| `USER_STACK` | Your backend stack | Python/FastAPI |
| `CAT_FACTS_API_URL` | Cat Facts API endpoint | https://catfact.ninja/fact |
| `API_TIMEOUT` | External API timeout (seconds) | 5 |
| `APP_NAME` | Application name | Dynamic Profile Endpoint |
| `APP_VERSION` | Application version | 1.0.0 |

## 🛡️ Error Handling

The API handles various error scenarios:

- **504 Gateway Timeout** - When Cat Facts API takes too long
- **503 Service Unavailable** - When Cat Facts API is down
- **500 Internal Server Error** - For unexpected errors

All errors are logged for debugging purposes.

## ✅ Acceptance Criteria

This implementation meets all requirements:

- ✅ Working GET `/me` endpoint returning 200 OK
- ✅ Response follows exact JSON schema
- ✅ All required fields present (status, user, timestamp, fact)
- ✅ User object contains email, name, and stack
- ✅ Timestamp in ISO 8601 UTC format
- ✅ Dynamic timestamp updates on each request
- ✅ Cat fact fetched from Cat Facts API
- ✅ Fresh cat fact on every request (not cached)
- ✅ Content-Type: application/json
- ✅ Well-structured code following best practices
- ✅ Proper error handling
- ✅ Logging for debugging
- ✅ CORS support
- ✅ Environment variable configuration

## 🔧 Development

### Running in Development Mode

```bash
uvicorn main:app --reload --log-level debug
```

### Viewing Logs

Logs are printed to the console with timestamps and log levels.

## 📚 Tech Stack

- **FastAPI** - Modern, fast web framework
- **Uvicorn** - ASGI server
- **HTTPX** - Async HTTP client
- **Pydantic** - Data validation
- **Python-dotenv** - Environment variable management

## 🤝 Contributing

Feel free to enhance this project by adding:
- Rate limiting
- Caching for cat facts (with TTL)
- Additional profile fields
- Unit tests
- Docker support

## 📝 License

This is a Stage 0 task project.

---

**Built with ❤️ using FastAPI**

