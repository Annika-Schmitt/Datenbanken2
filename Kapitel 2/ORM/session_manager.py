from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book

engine = create_engine(f"sqlite:///bookstore.db")
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

book = session.query(Book).first()
print(book.title)

session.add(Book("XY1234", "Some title", "AS1611"))
session.commit()

