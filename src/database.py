from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite engine instance
engine = create_engine("sqlite:///inventory.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_session():
    """
    Helper function to get database session.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
