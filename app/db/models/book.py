from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey('authors.id'))  # Связь с таблицей авторов
    available_copies = Column(Integer)

    author = relationship("Author", back_populates="books")
