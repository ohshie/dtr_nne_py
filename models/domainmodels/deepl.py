from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class Deepl(Base):
    __tablename__ = "deepl"

    def __eq__(self, other):
        if isinstance(other, Deepl):
            return self.__dict__ == other.__dict__

    ApiKey: Mapped[str] = mapped_column(primary_key=True)
