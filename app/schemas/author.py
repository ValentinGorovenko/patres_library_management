from pydantic import BaseModel
from typing import List, Optional


class AuthorBase(BaseModel):
    name: str
    biography: Optional[str] = None
    birth_date: str


class AuthorCreate(AuthorBase):
    pass  # Здесь можно добавить дополнительные поля


class Author(AuthorBase):
    id: int
    books: List[int] = []

    class Config:
        orm_mode = True
