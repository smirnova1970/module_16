"""Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по
значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом
user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}
Примечания:
Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.
Файл module_16_3.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него."""

from fastapi import FastAPI, HTTPException, Path
from typing import Dict
from pydantic import BaseModel, constr, conint

app = FastAPI()

# Словарь для хранения пользователей
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

# Модель для валидации данных пользователя
class User(BaseModel):
    username: constr(min_length=5, max_length=20)
    # username должен быть от 5 до 20 символов и содержать только буквы, цифры и подчеркивание
    age: conint(ge=18, le=120)  # age должен быть от 18 до 120

@app.get('/users')
async def get_user_page() -> Dict[str, str]:
    return users

@app.post('/user/{username}/{age}')
async def user_register(user: User) -> str:
    user_id = str(int(max(users.keys(), key=int)) + 1)
    users[user_id] = f'Имя: {user.username}, возраст: {user.age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user: User, user_id: int = Path(..., ge=1)) -> str:
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id_str] = f'Имя: {user.username}, возраст: {user.age}'
    return f'The user {user_id_str} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return f'User {user_id} has been deleted'
