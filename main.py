from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {"1": {"name": "Alice", "age": 30}, "2": {"name": "Bob", "age": 25}}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users/")
def create_user(user_id: str, name: str, age: int):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user_id] = {"name": name, "age": age}
    return users[user_id]