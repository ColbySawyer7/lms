import requests
from faker import Faker
import random
from datetime import datetime, timedelta

# Configuration
API_BASE_URL = "http://backend:8000"
TOTAL_BOOKS = 150
TOTAL_LIBRARIES = 50
TOTAL_USERS = 25
TOTAL_CHECKOUTS = 78

# Initialize Faker
fake = Faker()

USER_UUIDs = []

AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjZDdiZDg4Ny05Njg3LTQyODItYmQ4Zi1kMmYzZjIzYWFhMTAiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcxNTA0NTE0NH0.94JuluNrW_16FyGSB3LhUUixK7npgwbvMfDpnEVrt7I"

headers = {
    'Authorization': AUTH_TOKEN
}

def create_books():
    for _ in range(TOTAL_BOOKS):
        book_data = {
            "title": fake.sentence(),
            "author": fake.name(),
            "isbn": fake.isbn13(),
            "publication_date": fake.date_between(start_date="-10y", end_date="today").isoformat(),
            "genre": fake.word()
        }
        response = requests.post(f"{API_BASE_URL}/api/v1/books", json=book_data, headers=headers)
        print("Book Created:", response.json())

def create_libraries():
    for _ in range(TOTAL_LIBRARIES):
        library_data = {
            "name": fake.company(),
            "location": fake.address()
        }
        response = requests.post(f"{API_BASE_URL}/api/v1/libraries", json=library_data, headers=headers)
        print("Library Created:", response.json())

def create_users():
    for _ in range(TOTAL_USERS):
        user_data = {
            "email": fake.email(),
            "password": fake.password(),
        }
        response = requests.post(f"{API_BASE_URL}/api/v1/auth/register", json=user_data, headers=headers)
        USER_UUIDs.append(response.json().get('id'))
        print("User Created:", response.json())

def create_checkouts():
    # Simulate fetching random book, user, and library IDs
    book_ids = list(range(1, TOTAL_BOOKS + 1))
    library_ids = list(range(1, TOTAL_LIBRARIES + 1))

    for _ in range(TOTAL_CHECKOUTS):
        checkout_data = {
            "book_id": random.choice(book_ids),
            "user_id": random.choice(USER_UUIDs),
            "library_id": random.choice(library_ids),
            "checkout_date": fake.date_between(start_date="-1y", end_date="today").isoformat(),
            "due_date": (datetime.now() + timedelta(days=14)).isoformat(),  # 14 days from today
            "status": "Checked Out"
        }
        response = requests.post(f"{API_BASE_URL}/api/v1/transactions", json=checkout_data, headers=headers)
        print("Checkout Created:", response.json())

def main():
    create_books()
    create_libraries()
    create_users()
    print(USER_UUIDs)
    create_checkouts()

if __name__ == "__main__":
    main()
