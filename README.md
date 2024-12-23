# Multi-Model LLM pricing estimator REST API

## Overview
This project implements a REST API using FastAPI to calculate the number of tokens for text, audio, and image inputs across different models. The project uses `tiktoken` for tokenization and includes endpoints for health checks, authentication, and token calculations.

## Features
- **Text Token Calculation**: Supports models like GPT-3.5, GPT-4, and GPT-2.
- **Authentication**: OAuth2 token-based authentication.
- **Scalability**: Easily extendable for new models or input types.

## Project Structure
```
llm_pricing_estimator/
├── app/
│   ├── __init__.py
│   ├── main.py             # Main FastAPI application
│   ├── dependencies.py     # Authentication dependencies
│   ├── token_calculations.py # Token calculation logic
│   └── models.py           # Pydantic models for request validation
├── tests/
│   ├── __init__.py
│   ├── test_text_tokens.py # Tests for text token calculation
│   ├── test_audio_tokens.py # Placeholder for audio token tests
│   ├── test_image_tokens.py # Placeholder for image token tests
│   └── test_health_check.py # Health check tests
├── requirements.txt        # Dependencies
├── README.md               # Documentation
└── .env                    # Environment variables
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/llm_pricing_estimator
   cd llm_pricing_estimator
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with the following content:
   ```env
   SECRET_TOKEN=my_secure_token
   ```

## Running the Application
Run the FastAPI application with Uvicorn:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints
### Health Check
- **Endpoint**: `/health`
- **Method**: GET
- **Description**: Checks the health of the API.

### Text Token Calculation
- **Endpoint**: `/text_tokens`
- **Method**: POST
- **Request Body**:
  ```json
  {
      "text": "Your input text",
      "model_name": "gpt-3.5"
  }
  ```
- **Response**:
  ```json
  {
      "tokens": 42
  }
  ```

### Audio and Image Token Calculation
Currently not supported.

## Testing
Run tests using `pytest`:
```bash
pytest tests/
```