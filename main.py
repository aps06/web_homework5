import asyncio
from all_API import PrivatBankAPI
from datetime import datetime, timedelta

API = PrivatBankAPI()


class DataHandler:

    @staticmethod
    async def give_date(num: int) -> list:
        list_date = []

        for i in range(1, num + 1):
            new_date = datetime.now() - timedelta(days=i)
            list_date.append(datetime.strftime(new_date, "%d.%m.%Y"))

        return list_date

    @staticmethod
    async def format_currency_rates(exchange_rates: dict) -> dict:
        list_of_currencies = ["USD", "EUR"]
        course = {}
        for i in exchange_rates["exchangeRate"]:
            for rate in list_of_currencies:
                if i["currency"] == rate:
                    course.update(
                        {
                            rate: {
                             "sale": i["saleRateNB"],
                             "purchase": i["purchaseRateNB"],
                            }
                        }
                    )
        return course


def decor(f):
    async def _fn():
        try:
            print(await f())
        except Exception as e:
            print(e)
    return _fn


@decor
async def main():
    num = int(input("give number (1-10) >>> "))
    if 0 < num <= 10:
        dict_rates = {}

        for date in await DataHandler.give_date(num):
            exchange_rates = await API.get_exchangeRate(date)

            dict_rates[date] = await DataHandler.format_currency_rates(exchange_rates)

        return dict_rates
    raise ValueError


if __name__ == "__main__":
    asyncio.run(main())
