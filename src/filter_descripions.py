import re
from typing import Any


def filter_transactions_by_description(transactions: Any) -> Any:
    """
    Сортировка по опр. слову
    """
    filtered_transactions = []
    uns = input("Отсортировать по опр слову? \n").upper()
    while uns not in ("ДА", "НЕТ"):
        uns = input("Нет такого варианта ответа, попробуйте снова (ДА/НЕТ): ")
        uns = uns.upper()
    if uns == "ДА":
        search_string = input("Введите слово: ")
        for transaction in transactions:
            if re.search(search_string, transaction["description"], re.IGNORECASE):
                filtered_transactions.append(transaction)
        print(f"Операции отфильтрованы по описанию {search_string}")
        return filtered_transactions
    else:
        return transactions
