from pydantic import BaseModel


class NewsOutletDTO(BaseModel):
    inUse: bool
    alwaysJs: bool
    name: str
    website: str
    mainPageCss: str
    newsPageCss: str
