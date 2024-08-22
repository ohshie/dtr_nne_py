from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ChatGptModel(Base):
    __tablename__ = "chatgpt"

    def __eq__(self, other):
        if isinstance(other, ChatGptModel):
            return self.__dict__ == other.__dict__

    ApiKey: Mapped[str] = mapped_column(primary_key=True)
