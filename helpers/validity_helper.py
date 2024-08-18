from models.domainmodels.newsoutlet import NewsOutlet

from urllib.parse import urlparse


def is_valid_str_field(field: str) -> bool:
    if field == "":
        return False
    if not isinstance(field, str):
        return False
    if str.isspace(field):
        return False
    return True


def is_valid_outlet_object(outlet: NewsOutlet) -> bool:
    return all(
        [
            is_valid_str_field(outlet.name),
            urlparse(outlet.website).scheme,
            is_valid_str_field(outlet.newsPageCss),
            is_valid_str_field(outlet.mainPageCss),
        ]
    )
