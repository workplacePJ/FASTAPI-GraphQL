import strawberry
from .company import Company

@strawberry.type
class Query:
    @strawberry.field
    async def company(self) -> Company:
        return Company(id = 1, name = '株式会社トータルメディエイト', postalCode = '1140034', address = '東京都北区上十条2-25-4')
