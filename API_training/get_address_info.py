from pprint import pprint

from aiohttp import ClientSession


class NominatimAPI:

    Base_URL: str = "https://nominatim.openstreetmap.org"

    @staticmethod
    def create_session(func):
        async def wrapper(**kwargs):
            async with ClientSession(base_url=NominatimAPI.Base_URL) as session:
                return await func(**kwargs, session=session)
        return wrapper

    @staticmethod
    @create_session
    async def search_address(city: str,
                             street: str,
                             formate: str,
                             country: str,
                             session: ClientSession = None,
                             ):
        params = {}
        if country:
            params["country"] = country
        if formate:
            params["format"] = formate
        if city:
            params["city"] = city
        if street:
            params["street"] = street

        response = await session.get(
            url="/search",
            params=params
        )
        # if response.status == 200:
        pprint(await response.json())
        return await response.json()
