from dotenv import load_dotenv 
import os 
load_dotenv()

DB_NAME = os.environ.get("DB_NAME") 
DB_USER = os.environ.get("DB_USER") 
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get('DB_HOST')

AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
ALGORITHMS = os.environ.get("ALGORITHMS")
API_AUDIENCE = os.environ.get("API_AUDIENCE")
CLIENT_ID = os.environ.get("CLIENT_ID")
LOGOUT_REDIRECT_URI = os.environ.get("LOGOUT_REDIRECT_URI")
TOKEN_CASTING_DIRECTOR = os.environ.get("TOKEN_TEST")
TOKEN_CASTING_ASSISTANT = os.environ.get("TOKEN_TEST_2")
TOKEN_EXPIRED = os.environ.get("TOKEN_EXPIRED")

BLACKLISTED_TOKENS = set()