from models.domainmodels.newsoutlet import NewsOutlet
from models.dto.newsoutlet_dto import NewsOutletDTO


def map_newsoutlet_dto_to_domain(outlets_dto: list[NewsOutletDTO]) -> list[NewsOutlet]:
    news_outlets: list[NewsOutlet] = []

    for outlet_dto in outlets_dto:
        mapped_outlet = NewsOutlet(
            name=outlet_dto.name,
            website=outlet_dto.website,
            newsPageCss=outlet_dto.newsPageCss,
            mainPageCss=outlet_dto.mainPageCss,
            alwaysJs=outlet_dto.alwaysJs,
            inUse=outlet_dto.inUse,
        )

        news_outlets.append(mapped_outlet)

    return news_outlets


def map_domainoutlets_to_DTO(newsoutlets: list[NewsOutlet]) -> list[NewsOutletDTO]:
    news_outlets_dto: list[NewsOutletDTO] = []

    for newsoutlet in newsoutlets:
        mapped_outlet = NewsOutletDTO(
            name=newsoutlet.name,
            website=newsoutlet.website,
            newsPageCss=newsoutlet.newsPageCss,
            mainPageCss=newsoutlet.mainPageCss,
            alwaysJs=newsoutlet.alwaysJs,
            inUse=newsoutlet.inUse,
        )

        news_outlets_dto.append(mapped_outlet)

    return news_outlets_dto
