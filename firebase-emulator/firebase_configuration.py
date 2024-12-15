import firebase_admin
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import json
import os

load_dotenv()
FIREBASE_SERVICE_ACCOUNT_KEY = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")
info = json.loads(FIREBASE_SERVICE_ACCOUNT_KEY)
cred = credentials.Certificate(info)
firebase_admin.initialize_app(cred)