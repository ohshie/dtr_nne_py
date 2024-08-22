from __future__ import annotations

from typing import TypeVar, Generic

from models.domainmodels.deepl import Deepl
from models.domainmodels.newsoutlet import NewsOutlet
from models.domainmodels.zenrows import Zenrows
from models.domainmodels.chatgptmodel import ChatGptModel

T = TypeVar("T")


def provide_tablename(model: Generic[T]) -> Generic[T] | None:
    if model is NewsOutlet:
        tablename = "newsoutlets"
    elif model is Zenrows:
        tablename = "zenrows"
    elif model is Deepl:
        tablename = "deepl"
    elif model is ChatGptModel:
        tablename = "chatgpt"

    else:
        tablename = None

    return tablename
