"""
Импортируем ранее сделанные функции
"""


def masks_of_cards(data: str) -> str:
    """
    Функция переиспользует ранее написанные функции
    и возвращает исходную строку с замаскированным номером карты/счета.fla
    """
    split_data = data.split(" ")
    if split_data[0] == "Счет":
        last_spliter = split_data[-1]
        masked_account = f"Cчет **{last_spliter[-4:]}"
        return masked_account
    else:
        last_spliter = split_data[-1]
        masked_card = f"{split_data[:-1]} {last_spliter[:4]} {last_spliter[4:7]}** **** {last_spliter[-4:]}"
        return masked_card


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
