from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Author, Info, Publisher

engine = create_engine(f"sqlite:///bookstore.db")
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Create SQL statement in queries
results = session.query(Book).all()
for row in results:
    print("BookID: ", row.BookID, "Title:", row.Title, "AuthorID:", row.AuthorID)

results = session.query(Book).filter_by(AuthorID='KD840').all()
for row in results:
    print("Book written by Author with ID = KD840: ", row.Title)
