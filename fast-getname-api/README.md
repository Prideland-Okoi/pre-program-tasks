# Fast Full Name API

This project is a simple API built with FastAPI to handle user information, specifically their first and last names.

## Features

- Allows users to submit their first and last names.
- Validates user input to ensure non-empty names.
- Returns the full name of the user upon request.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/prideland-okoi/fast-fullname-api.git
   ```

2. Install the required dependencies:

   ```bash
   cd fast-fullname-api
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2a. Navigate to `http://127.0.0.1:8000/docs` in your web browser to access the Swagger UI for interacting with the API. or

2b. Open another terminal and run the curl command

```bash
curl -X 'POST' \
 'http://localhost:8000/get_fullname/' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
"first_name": "Prideland",
"last_name": "Okoi"
}'

```

3. Use the provided endpoints to submit user information and retrieve full names.

## API Endpoints

- **POST /api/get_fullname/**: Get the full name of a user.

## Documentation

For more detailed information about the API endpoints, models, validators, and implementation details, please refer to the [documentation.md](https://github.com/Prideland-Okoi/pre-program-tasks/upload/task_2/fast-getname-api/documentation.md) file.

## Files

| Task                                                                                                                         | scripts           |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| From the video shown, create a simple fast API that takes the first and last name of a user and returns the user's full name | `get_fullname.py` |

````

|```
````
