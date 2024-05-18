# import requests
#
#
# def get_usd_rub_rate(from_currency, amount) -> float:
#     """
#     Получает обменный курс USD к RUB.
#     Returns:
#         float: Обменный курс USD к RUB, или 0.0, если возникла ошибка.
#     """
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
#     payload = {}
#     headers = {
#         "apikey": "ntAaWNz5Fhxs6dQLnlD6BA3OYXCGm810"
#     }
#     response = requests.request("GET", url, headers=headers, data=payload)
#     if response.status_code == 200:
#         data = response.json()
#         return float(data.get('result', 0.0))
#     else:
#         print(f"Ошибка запроса: {response.status_code}")
#         return 0.0
#
#
# # Пример использования
# rate = get_usd_rub_rate("USD", 10)
# print(rate)
# import os
# from dotenv import load_dotenv
# load_dotenv()
# # Получение значения переменной GITHUB_TOKEN из .env-файла
# API_KEY = os.getenv('API_KEY')
# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# dollar_rate = float(data['Valute']['USD']['Value'])
# print(dollar_rate)
