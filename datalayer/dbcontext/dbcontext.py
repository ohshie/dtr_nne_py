import os
import shutil

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker


def get_db_session():
    db_path = "dtr_nne.db"
    if os.getenv("PYTHON_ENV") == "test":
        source_db = os.path.abspath("../../dtr_nne.db")
        if os.path.getmtime(source_db) > os.path.getmtime("../dtr_nne.db"):
            shutil.copy2(source_db, "../dtr_nne.db")
        db_path = "../dtr_nne.db"

    engine = create_engine(f"sqlite:///{db_path}")
    session = sessionmaker(bind=engine)
    return session()
