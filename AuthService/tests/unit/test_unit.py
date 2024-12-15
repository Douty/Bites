from fastapi.testclient import TestClient
from app.main import app
import pytest
from firebase_admin import auth
from httpx import AsyncClient, Client
import os

from dotenv import load_dotenv

load_dotenv()


client = TestClient(app)





def test_system_check():
    res= client.get('/')
    assert res.status_code == 200
    assert res.json() == {"message": "Auth service is up and running!"}


