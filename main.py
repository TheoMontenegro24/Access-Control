from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class LoginUser(BaseModel):
    email: str
    contra: str
user_dtb={
        "email":"theo.montenegro@gmail.com",
        "contra":"Admin123"
    }



@app.post("/login")
def login (user: LoginUser):
    if user==user_dtb["email"] and user.contra ==user_dtb["contra"]:
        return {"mensaje":"Login exitoso"}
    else:
        return {"mensaje": "Login ni exitoso"}
