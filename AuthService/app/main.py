from fastapi import FastAPI, status,HTTPException, Security
from fastapi.security import HTTPBearer
from pydantic import BaseModel, EmailStr
from firebase_setup import auth
from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()

auth_emulator = os.getenv("FIREBASE_AUTH_EMULATOR_HOST")
if auth_emulator:
    print(f"Connected to Firebase Auth Emulator at {auth_emulator}")
else:
    print("Connected to Real Firebase Auth")

class UserRegister(BaseModel):
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str

security = HTTPBearer()

@app.get("/")
def root():
    return {"message": "Auth service is up and running!"}

@app.post("/auth/registry",status_code=201)
async def register(user:UserRegister):
    try:
        created_user = auth.create_user(email=user.email,password=user.password)
        return {"message": "User registered successfully", "user_id": created_user.uid}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Unexpected error: {str(e)} ")



@app.post("/auth/verify",status_code=200)
async def verify(authorization: str = Security(security)):
    try:
        token = authorization.credentials
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Unexpected error: {str(e)} ")