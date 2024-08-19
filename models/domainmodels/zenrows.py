from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Zenrows(Base):
    __tablename__ = "zenrows"

    def __eq__(self, other):
        if isinstance(other, Zenrows):
            return self.ApiKey == other.ApiKey
        return False

    ApiKey: Mapped[str] = mapped_column(primary_key=True)
