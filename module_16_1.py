
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Главная страница"}

@app.get("/user/admin")
async def get_admin():
    return {"Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def get_user(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def get_user_info(username: str = 'Timmi', age: int = 34):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


