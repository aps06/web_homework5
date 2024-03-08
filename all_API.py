import aiohttp
from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    async def get_exchangeRate(self, date_list: list[str]) -> str:
        pass


class PrivatBankAPI(API):

    async def get_exchangeRate(self, date: str) -> dict:
        _url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
        async with aiohttp.ClientSession() as session:
            async with session.get(_url) as response:
                result = await response.json()
        return result
