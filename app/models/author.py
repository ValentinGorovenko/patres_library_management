from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from app.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    biography = Column(Text)
    birth_date = Column(Date)

    books = relationship("Book", back_populates="author")
