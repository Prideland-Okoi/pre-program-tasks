# Fast Full Name, PDF Upload API and READ PDF content API

This project encompasses three APIs built with FastAPI - one for handling user information, specifically their first and last names, the second one for handling PDF file uploads and retrieval and the other allows you to read the content of a PDF file..


## Fast Full Name API
This project is a simple API built with FastAPI to handle user information, specifically their first and last names.

### Features

- Allows users to submit their first and last names.
- Validates user input to ensure non-empty names.
- Returns the full name of the user upon request.

### Requirements

- Python 3.10
- FastAPI
- Uvicorn (ASGI server)
- Pydantic

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/prideland-okoi/task_2/fast-getname-api.git
   ```

2. Install the required dependencies:

   ```bash
   cd fast-getname-api
   pip install -r requirements.txt
   ```

### Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2a. Navigate to `http://127.0.0.1:8000/docs` or hosted website `https://get-name-api.onrender.com/docs` in your web browser to access the Swagger UI for interacting with the API. or

2b. Open another terminal and run the curl command

```bash
curl -X 'POST' \
 'http://localhost:8000/api/get_fullname/' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
"first_name": "Prideland",
"last_name": "Okoi"
}'

```

3. Use the provided endpoints to submit user information and retrieve full names.

### API Endpoints

- **POST /api/get_fullname/**: Get the full name of a user.

### Documentation

For more detailed information about the API endpoints, models, validators, and implementation details, please refer to the [documentation.md](https://github.com/Prideland-Okoi/pre-program-tasks/upload/task_2/fast-getname-api/DOCUMENTATION.md) file.

### Files

| Task                                                                                                                         | scripts           |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| From the video shown, create a simple fast API that takes the first and last name of a user and returns the user's full name | `get_fullname.py` |

## File Upload and Retrieval API

This is a simple API built with FastAPI that allows users to upload PDF files and retrieve them.

### Features

- **File Upload**: Users can upload PDF files. Only PDF files are allowed and there is a maximum file size limit of 5 MB.
- **File Retrieval**: Users can retrieve uploaded PDF files.

### Requirements
- fastapi
- uvicorn
- Werkzeug
- python-multipart

### Setup

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI server with `uvicorn main:app --reload`.

### Usage

#### File Upload

Endpoint: `POST /api/upload_pdf/`

Upload a PDF file using a `multipart/form-data` request. The request should contain a file parameter named `file`.

Example:

```bash
curl -X POST -F "file=@/path/to/file.pdf" http://localhost:8000/api/upload_pdf/
```

#### File Retrieval

Endpoint: `GET /api/get_pdf/{filename}`

Retrieve a previously uploaded PDF file by providing its filename.

Example:

```bash
curl http://localhost:8000/api/get_pdf/Devops_in_Python.pdf --output Devops_in_Python.pdf
```

#### List Uploaded PDF Files

Endpoint: `GET /api/list_pdfs/`

Retrieve a list of PDF files uploaded to the server along with their creation dates.

Example:

```bash
curl http://localhost:8000/api/list_pdfs/
```

### Error Handling

- **400 Bad Request**: Returned if a non-PDF file is uploaded.
- **413 Payload Too Large**: Returned if the uploaded file exceeds the maximum size limit.
- **409 Conflict**: Returned if the file already exists.
- **404 Not Found**: Returned if the requested file is not found.
- **500 Internal Server Error**: Returned if there is any server-side error.
  
### Files
| Task| scripts           |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------- |
|In your last program, you created an API to join words. In this task, create an API endpoint that collects a PDF file and stores that file to disk.|`get_pdf.py`|

## PDF Reader API

This API endpoint allows you to read the content of a PDF file.

### Usage

#### Read contents of PDF file
Endpoint: `GET /api/read_pdf/{filename}`

Reads the content of a PDF file.

Example

```bash
curl -X GET http://localhost:8000/api/read_pdf/devops_in_python.pdf
```

### Response:
  - **200 OK**: Returns the text content extracted from the PDF file.
  - **404 Not Found**: If the requested file is not found.
  - **500 Internal Server Error**: If there's an error during processing.

### Files
| Task| scripts           |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------- |
|In your api endpoint that collects a pdf file, create a reader that reads the pdf and returns the data as given in the example attached to this tasks.|`read_pdf.py`|
