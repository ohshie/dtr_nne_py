from symtable import Class

from mappers.model_tablename_mapper import provide_tablename
from models.domainmodels.newsoutlet import NewsOutlet


def test_tablename_mapper_base():
    tablename = provide_tablename(NewsOutlet)

    assert tablename is not None
    assert tablename == "newsoutlets"


def test_tablename_mapper_faulty():
    tablename = provide_tablename(Class)

    assert tablename is None
