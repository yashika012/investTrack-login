import os
from dotenv import load_dotenv

# .env file ka full path resolve karo — chahe kisi bhi directory se run karo
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

BASE_URL = os.getenv("BASE_URL")

INVESTOR = {
    "email": os.getenv("INVESTOR_EMAIL"),
    "password": os.getenv("INVESTOR_PASSWORD")
}

ADMIN = {
    "email": os.getenv("ADMIN_EMAIL"),
    "password": os.getenv("ADMIN_PASSWORD")
}

#debug
if __name__ == "__main__":
    print(f"BASE_URL     : {BASE_URL}")
    print(f"INVESTOR     : {INVESTOR}")
    print(f"ADMIN        : {ADMIN}")