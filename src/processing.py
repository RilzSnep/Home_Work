from operator import itemgetter
from typing import Any, Dict, List


def filter_by_state(list_with_dictionary: List[Dict], values: str = "EXECUTED") -> list:
    return [item for item in list_with_dictionary if item.get("state") == values]


def sort_by_data(list_with_data_in_dictionary: Any, rever: bool = True) -> Any:
    """
    Функция, которая сортирует список словарей по дате
    """
    sorter = sorted(list_with_data_in_dictionary, key=itemgetter("date"), reverse=rever)
    return sorter
