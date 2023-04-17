from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "Books"
    book_id = Column(String, primary_key=True)
    author_id = Column(String, ForeignKey("author.author_id"))
    title = Column(String)


class Author(Base):
    __tablename__ = "Author"
    author_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)
    country = Column(String)
