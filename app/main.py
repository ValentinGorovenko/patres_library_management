from fastapi import FastAPI
from app.routers import books, authors, users

app = FastAPI()

app.include_router(books.router)
app.include_router(authors.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
