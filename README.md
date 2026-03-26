# FastAPI demo for interview task

Simple API created in FastAPI with integration tests in pytest.

## Run API
```bash
fastapi dev main.py
```

## Run tests
```bash
pytest
```

## Endpoints

### GET /
Returns basic information that the API is running.

Example response:
```json
{"message": "Tesena test API is running!"}
```

### POST /discount
Accepts original price and discount percent, then returns saved amount and final price.

Example request:
```json
{"original_price": 1000, "discount_percent": 20}
```

Example response:
```json
{"original_price": 1000.0, "discount_percent": 20.0, "saved_amount": 200.0, "final_price": 800.0}
```

### POST /password-check
Checks whether a password is strong enough based on basic rules.

Example request:
```json
{"password": "Test123!"}
```

Example response:
```json
{
  "is_strong": true,
  "checks": {
    "has_min_length": true,
    "has_uppercase": true,
    "has_lowercase": true,
    "has_digit": true,
    "has_special": true
  }
}
```

## Test coverage
- GET / returns 200 and expected response body
- POST /discount returns correct calculated values
- POST /discount returns 422 for invalid discount percent
- POST /password-check returns `is_strong: true` for a strong password
- POST /password-check returns `is_strong: false` for a weak password
- POST /password-check returns 422 for empty password

## Postman collection
Repository also contains a Postman collection for manual API testing.

Location:
`postman/tesena-api.postman_collection.json`