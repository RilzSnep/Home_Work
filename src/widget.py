from src.masks import account_mask, card_mask

"""
Импортируем ранее сделанные функции
"""


def masks_of_cards(number_card_or_bill_number: str) -> str:
    """
    Функция, чтобы отличить и замаскировать номер карты/счёта
    """
    number_card_or_bill_number_split = number_card_or_bill_number.split(" ")
    if number_card_or_bill_number_split[0] == "Счет":
        return f"{number_card_or_bill_number_split[0]} {account_mask(number_card_or_bill_number_split[-1])}"
    else:
        return f'{" ".join(number_card_or_bill_number_split[:-1])} {card_mask(number_card_or_bill_number_split[-1])}'


def dates(date: str) -> str:
    """
    Функция, чтобы определить дату
    """
    date_split = date.split("T")[0].split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"


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
