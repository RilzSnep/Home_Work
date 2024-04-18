from operator import itemgetter


def filter_by_state(list_with_dictionary: list, values: str = "EXECUTED") -> list:
    """
    Функция, которая фильтрует список словарей
    """
    list_executed = []
    for dictionary in list_with_dictionary:
        if dictionary["state"] == values:
            list_executed.append(dictionary)
    return list_executed


def sort_by_data(list_with_data_in_dictionary: list) -> list:
    """
    Функция, которая сортирует список словарей по дате
    """
    sorter = sorted(list_with_data_in_dictionary, key=itemgetter("date"), reverse=True)
    return sorter
