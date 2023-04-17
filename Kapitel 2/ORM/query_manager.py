import sqlalchemy
import session_manager
from models import Author, Book, Info, Publisher

session = session_manager.setup()

results = session.query(Author).all()
print(results)

