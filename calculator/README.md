# Average Calculator Microservice

## Overview
This Django-based microservice fetches numbers (Prime, Fibonacci, Even, Random) from a test server, maintains a sliding window of unique numbers, and calculates their average.

## Features
- Fetches numbers from a third-party API.
- Maintains a sliding window of the latest numbers.
- Calculates and returns the average of stored numbers.
- Ensures responses are processed within 500ms.

## Setup & Installation
### 1. Clone Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/RA2211027010133.git
cd RA2211027010133
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install django djangorestframework requests
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start Server
```bash
python manage.py runserver
```

## API Endpoints
### 1. Register Company
```http
GET /register/
```
**Response:**
```json
{
  "companyName": "Affordmedical",
  "clientID": "your_client_id",
  "clientSecret": "your_client_secret",
  "ownerName": "dev",
  "ownerEmail": "dr3282@srmist.edu.in",
  "rollNo": "RA2211027010133"
}
```

### 2. Get Authorization Token
```http
GET /auth/
```
**Response:**
```json
{
  "token_type": "Bearer",
  "access_token": "your_access_token"
}
```

### 3. Fetch Numbers & Calculate Average
```http
GET /numbers/{type}/
```
**{type} options:**
- `p` - Prime numbers
- `f` - Fibonacci numbers
- `e` - Even numbers
- `r` - Random numbers

**Example Response:**
```json
{
  "windowPrevState": [2, 4, 6, 8],
  "windowCurrState": [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
  "numbers": [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
  "avg": 23.40
}
```

## Testing with Postman
1. Import the API URLs into Postman.
2. Send `GET` requests to the respective endpoints.
3. Observe the response for number fetching and averaging.

## Deployment
For production, use `gunicorn` and configure a cloud service such as AWS or Heroku.

## Author
**Devesh Ruttala**

## License
This project is licensed under the MIT License.

