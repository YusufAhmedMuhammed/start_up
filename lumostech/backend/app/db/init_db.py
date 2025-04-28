from sqlalchemy import create_engine
from app.core.config import settings
from app.db.base_class import Base
from app.models.lead import Lead

def init_db():
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db() 