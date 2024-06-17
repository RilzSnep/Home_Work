import re
from collections import Counter
from typing import Any, Dict, List


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


def categorize_transactions(transactions: List[Dict[str, Any]], categories_2: Dict[str, List[str]]) -> Dict[str, int]:
    counts_category: Dict[str, int] = Counter()
    for transaction in transactions:
        if "description" in transaction:
            for cat, ke in categories_2.items():
                if any(keyword.lower() in transaction["description"].lower() for keyword in ke):
                    counts_category[cat] += 1
                    break
    return dict(counts_category)
