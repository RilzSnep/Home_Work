from operator import itemgetter


def sort_by_state(list_with_dictionary: list, values: str = "EXECUTED") -> list:
    list_executed = []
    for dictionary in list_with_dictionary:
        if dictionary["state"] == values:
            list_executed.append(dictionary)
    return list_executed


def sort_by_data(list_with_data_in_dictionary: list) -> list:
    sorter = sorted(list_with_data_in_dictionary, key=itemgetter("date"), reverse=False)
    return sorter
