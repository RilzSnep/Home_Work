import json
import os

import requests
from dotenv import load_dotenv

from src.logger import logger_setup

load_dotenv()
logger = logger_setup()
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
    logger.info(f"1{from_currency} = {dollar_rate}RUB".encode("utf-8"))
    return total


def load_transactions(filepath: str) -> list:
    """
    function to load transactions
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("return the transaction".encode("utf-8"))
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        logger.error("Error json file")
        return []


def get_amount(dictionary: dict) -> float:
    """
    function to get amount from dictionary and convertation from USD to RUB
    """
    if dictionary["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("return the amount from dictionary RUB")
        return float(dictionary["operationAmount"]["amount"])
    else:
        from_cur = dictionary["operationAmount"]["currency"]["code"]
        amou = float(dictionary["operationAmount"]["amount"])
        result = get_usd_rub_rate(from_cur, amou)
        logger.info(f"return the amount from dictionary {from_cur}")
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


# get_usd_rub_rate("USD", 10)
# get_amount(valve)
