from fastapi.testclient import TestClient
from app.main import app
import pytest
from firebase_admin import auth
from httpx import AsyncClient, Client
import os

from dotenv import load_dotenv

load_dotenv()


host = os.getenv("FIREBASE_AUTH_EMULATOR_HOST")
client = TestClient(app)

# @pytest.mark.asyncio
# async def gen_token():
#     API_KEY = os.getenv("FIREBASE_WEB_API_KEY")
#     url = f"http://{host}/emulator/v1/accounts:signUp?key={API_KEY}"
#     payload = {
#         "email": "test@example.com",
#         "password": "password123",
#         "returnSecureToken": True
#     }
#     async with AsyncClient() as ac:
#         res = await ac.post(url,json=payload)
#         if res.status_code == 200:
#             res_data = res.json()
#             print(res_data)
#             return res_data["idToken"]


def test_register_user_test():
    user = {
        "email":"test@testemail.com",
        "password":"testtesttest"
    }
    
    res = client.post("/auth/registry",json=user)
    assert res.status_code == 201
    res_data = res.json()
    assert "message" in res_data and res_data["message"] == "User registered successfully" 
    created_user = auth.get_user_by_email("test@testemail.com")
    auth.delete_user(created_user.uid)
    


# @pytest.mark.asyncio
# async def test_validate_user_token():
#     token = await gen_token()
    
#     headers = {"Authorization": f"Bearer {token}"}
#     res = client.post("/auth/verify",headers=headers)

#     assert res.status_code == 200
#     res_data = res.json()
#     assert "uid" in res_data
#     assert res_data["email"] == "test@example.com"

