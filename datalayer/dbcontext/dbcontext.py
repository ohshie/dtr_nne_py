import os
import shutil

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

def get_db_session():
    if(os.getenv("PYTHON_ENV") == "test"):
        source_db = os.path.abspath('../../dtr_nne.db')
        shutil.copy2(source_db, 'dtr_nne.db')

    engine = create_engine('sqlite:///dtr_nne.db')
    session = sessionmaker(bind=engine)
    return session()