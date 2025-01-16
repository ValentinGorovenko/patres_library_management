from pydantic import BaseModel
from typing import List, Optional


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    publication_date: str
    available_copies: int


class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
