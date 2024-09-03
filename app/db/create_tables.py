from sqlalchemy import create_engine
from app.db.models.base import Base
from app.core.config import settings

# Create a SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)


def create_tables():
    # Create all tables defined by the Base metadata
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
