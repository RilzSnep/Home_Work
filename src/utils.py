import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
API_KEY = os.getenv("API_KEY")


def get_usd_rub_rate(from_currency: str, amount: float) -> float:
    """
    Получает обменный курс USD к RUB.
    Returns:
        float: Обменный курс USD к RUB, или 0.0, если возникла ошибка.
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
    payload: dict = {}
    headers = {"apikey": API_KEY}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return float(data.get("result", 0.0))
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return 0.0


def load_transactions(filepath: str) -> list:
    """
    function to load transactions
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def get_amount(dictionary: dict) -> float:
    """
    function to get amount from dictionary and convertation from USD to RUB
    """
    if dictionary["operationAmount"]["currency"]["code"] == "RUB":
        return float(dictionary["operationAmount"]["amount"])
    else:
        from_cur = dictionary["operationAmount"]["currency"]["code"]
        amou = float(dictionary["operationAmount"]["amount"])
        result = get_usd_rub_rate(from_cur, amou)
        return result


valve = {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
        "amount": "10",
        "currency": {
            "name": "USD",
            "code": "USD",
        },
    },
}

from_currenc = "USD"
amoun = 1
usd_rub_rate = get_usd_rub_rate(from_currenc, amoun)
print(f"Курс {from_currenc} к RUB: {usd_rub_rate}")

filepaths = "../data/operations.json"  # Путь к файлу с транзакциями
transactions = load_transactions(filepaths)
print(transactions)

print(get_amount(valve))
