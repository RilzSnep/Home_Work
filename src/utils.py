import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
API_KEY = os.getenv("API_KEY")


def get_usd_rub_rate(from_currency: str, amount: float) -> float:
    """
    Получает обменный курс USD или EUR к RUB.
    Returns:
        float: Обменный курс USD или EUR к RUB, или 0.0, если возникла ошибка.
    """
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    dollar_rate = float(data["Valute"][from_currency]["Value"])
    total = dollar_rate * amount
    return total


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
        "amount": "11",
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
