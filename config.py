import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

INVESTOR = {
    "email": os.getenv("INVESTOR_EMAIL"),
    "password": os.getenv("INVESTOR_PASSWORD")
}

ADMIN = {
    "email": os.getenv("ADMIN_EMAIL"),
    "password": os.getenv("ADMIN_PASSWORD")
}