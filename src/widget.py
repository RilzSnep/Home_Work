from src.masks import account_mask, card_mask

"""
Импортируем ранее сделанные функции
"""


def masks_of_cards(number_or_account: str) -> str:
    """
    Функция, чтобы отличить и замаскировать номер карты/счёта
    """
    _account = number_or_account.split(" ")
    if _account[0] == "Счет":
        return f"{_account[0]} {account_mask(_account[-1])}"
    else:
        return f'{" ".join(_account[:-1])} {card_mask(_account[-1])}'


def datetime_and_date(date_time: str) -> str:
    """
    Функция, чтобы определить дату
    """
    date_divided = date_time.split("T")[0].split("-")
    return f"{date_divided[2]}.{date_divided[1]}.{date_divided[0]}"


def mask_phone_numbers(text: str) -> str:
    """
    Функция, чтобы маскировать номера телефона в предложениях
    """
    words = text.split(" ")
    masked_text = []

    for word in words:
        if len(word) == 12 and word[0] == "+" and word[1:].isdigit():
            masked_word = word[:8] + "XXXX"
            masked_text.append(masked_word)
        elif len(word) == 13 and word[0] == "+" and word[-1] == ",":
            masked_word = word[:8] + "XXXX,"
            masked_text.append(masked_word)
        elif len(word) == 13 and word[0] == "+" and word[-1] == ".":
            masked_word = word[:8] + "XXXX."
            masked_text.append(masked_word)
        elif len(word) == 14 and word[0] == "+" and word[-1] == '"':
            masked_word = word[:8] + 'XXXX."'
            masked_text.append(masked_word)
        else:
            masked_text.append(word)

    return " ".join(masked_text)
