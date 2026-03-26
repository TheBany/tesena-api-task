from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Tesena test API is running!"}


class DiscountRequest(BaseModel):
    original_price: float = Field(gt=0)
    discount_percent: float = Field(ge=0, le=100)

class PasswordCheckRequest(BaseModel):
    password: str = Field(min_length=1)




@app.post("/discount")
def calculate_discount(data: DiscountRequest):
    saved_amount = round(data.original_price * (data.discount_percent / 100), 2)
    final_price = round(data.original_price - saved_amount, 2)

    return {
        "original_price": data.original_price,
        "discount_percent": data.discount_percent,
        "saved_amount": saved_amount,
        "final_price": final_price,
    }

@app.post("/password-check")
def password_check(data: PasswordCheckRequest):
    password = data.password

    has_min_length = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    is_strong = all(
        [
            has_min_length,
            has_uppercase,
            has_lowercase,
            has_digit,
            has_special,
        ]
    )

    return {
        "is_strong": is_strong,
        "checks": {
            "has_min_length": has_min_length,
            "has_uppercase": has_uppercase,
            "has_lowercase": has_lowercase,
            "has_digit": has_digit,
            "has_special": has_special,
        },
    }