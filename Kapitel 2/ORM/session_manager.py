from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


def setup():
    engine = create_engine(f"sqlite:///bookstore.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session
