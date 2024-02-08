# Fast Full Name API Documentation

## Introduction

This API provides functionality to handle user information, specifically their first and last names.

## Endpoints

### Get Full Name

- **URL:** `/api/get_fullname/`
- **Method:** `POST`
- **Request Body:** JSON object representing a user with `first_name` and `last_name` fields.
  ```json
  {
    "first_name": "Prideland",
    "last_name": "Okoi"
  }
  ```
- **Response:** JSON object containing the full name.
  ```json
  {
    "full_name": "John Doe"
  }
  ```

## Models

### User

Represents a user with a first name and a last name.

#### Properties

- `first_name` (string): The first name of the user.
- `last_name` (string): The last name of the user.

## Validators

### validate_name

Validates that the provided name is not empty.

#### Parameters

- `full_name` (string): The name to validate.

#### Raises

- `ValueError`: If the name is empty.

#### Returns

- `string`: The validated name.

## Implementation Details

- The API is implemented using FastAPI for handling HTTP requests.
- User input is validated using Pydantic models and validators to ensure data integrity.
