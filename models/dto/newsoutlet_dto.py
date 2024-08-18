from pydantic import BaseModel


class NewsOutletDTO(BaseModel):
    def __eq__(self, other):
        if isinstance(other, NewsOutletDTO):
            return self.website == other.website
        return False

    def __hash__(self):
        return hash(self.website)

    def to_dict(self):
        return {
            "name": self.name,
            "website": self.website,
            "mainPageCss": self.mainPageCss,
            "newsPageCss": self.newsPageCss,
            "inUse": self.inUse,
            "alwaysJs": self.alwaysJs,
        }

    inUse: bool
    alwaysJs: bool
    name: str
    website: str
    mainPageCss: str
    newsPageCss: str
