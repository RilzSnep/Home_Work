from src.masks import account_mask, card_mask


def masks_of_cards(data: str) -> str:
    """ "
    Функция, которая использует ранее написанные функции
    и возвращает исходную строку с замаскированным номером карты или счета.
    """
    right_data = data.split(" ")
    if right_data[0] == "Счет":
        return f"Счет {account_mask(right_data[-1])}"
    else:
        return f'{" ".join(right_data[:-1])} {card_mask(right_data[-1])}'


def datetime_to_date(datetime_string: str) -> str:
    """Функция, которая принимает строку и возвращает строку с датой"""
    date_parts = datetime_string.split("T")[0].split("-")
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
