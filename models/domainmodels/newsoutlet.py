from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase):
    pass

class NewsOutlet(Base):
    __tablename__ = 'NewsOutlets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    inUse: Mapped[bool] = mapped_column(default=False)
    alwaysJs: Mapped[bool] = mapped_column(default=False)
    name: Mapped[str] = mapped_column(default=None)
    website: Mapped[str] = mapped_column(default=None)
    mainPageCss: Mapped[str] = mapped_column(default=None)
    newsPageCss: Mapped[str] = mapped_column(default=None)