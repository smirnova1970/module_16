"""Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
1. id - номер пользователя (int)
2. username - имя пользователя (str)
3. age - возраст пользователя (int)
Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
1. Добавляет в список users объект User.
2. id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
3. Все остальные параметры объекта User - переданные в функцию username и age соответственно.
4. В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
1. Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
2. В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
1. Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
2. В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием
"User was not found" и кодом 404"""


from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int = None

@app.get('/users')
async def get_user_page() -> list:
    return users

@app.post('/user/{username}/{age}')
async def user_register(user: User, username: str, age: int):
    user_id= str(int(max(users, key=int))+1)
    users[user_id]=f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id]=f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'
