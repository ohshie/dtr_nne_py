from pydantic import BaseModel


class NewsOutletDTO(BaseModel):
    def __eq__(self, other):
        if isinstance(other, NewsOutletDTO):
            return self.website == other.website
        return False

    def __hash__(self):
        return hash(self.website)

    inUse: bool
    alwaysJs: bool
    name: str
    website: str
    mainPageCss: str
    newsPageCss: str
