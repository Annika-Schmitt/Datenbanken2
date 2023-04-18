import sqlalchemy.orm
from sqlalchemy import Column, String, ForeignKey

Base = sqlalchemy.orm.declarative_base()


class Book(Base):
    __tablename__ = "Book"
    BookID = Column(String, primary_key=True)
    Title = Column(String)
    AuthorID = Column(String, ForeignKey("Author.AuthorID"))


class Author(Base):
    __tablename__ = "Author"
    AuthorID = Column(String, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Birthday = Column(String)
    Country = Column(String)


class Info(Base):
    __tablename__ = "Info"
    BookID = Column(String, primary_key=True)
    Genre = Column(String)

class Publisher(Base):
    __tablename__ = "Publisher"
    PublisherID = Column(String, primary_key=True)
    PublishingHouse = Column(String)
    State = Column(String)
    Country = Column(String)
    YearEstablished = Column(String)
