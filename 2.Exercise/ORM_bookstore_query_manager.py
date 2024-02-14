from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Books

engine = create_engine(f"sqlite:///bookstore.db")
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Create SQL statement in queries
book = session.query(Books).first()
print(book.title)

session.add(Books("AB1234", "some title", "CD1234"))
session.commit()

results = session.query(Books).all()
for book in results:
    print("BookID: ", book.BookID, "Title:", book.Title, "AuthorID:", book.AuthorID)

results = session.query(Books).filter_by(AuthorID='KD840').all()
for book in results:
    print("Book written by Author with ID = KD840: ", book.Title)
