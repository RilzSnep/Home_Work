from src.logger import logger_setup

logger = logger_setup()


def card_mask(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) == 16:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info("Function mask_credit_card_number completed successfully")
        return masked_number
    else:
        logger.error("With the function mask_credit_card_number something is wrong")
    return card_number


def account_mask(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает ее маску"""
    if len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        logger.info("Function mask_account_number completed successfully")
        return masked_number
    else:
        logger.error("With the function mask_account_number something is wrong")
    return account_number


def mask_for_all(masked_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masker = masked_number.split(" ")
    msak = masker[-1]
    if len(msak) == 16:
        masked_number = f"{msak[:4]} {msak[4:6]}** **** {msak[-4:]}"
        logger.info("Function mask_credit_card_number completed successfully")
        return f"{' '.join(masker[:-1])} {masked_number}"
    elif len(msak) == 20:
        masked_number = f"**{msak[-4:]}"
        logger.info("Function mask_account_number completed successfully")
        return f"{' '.join(masker[:-1])} {masked_number}"
    else:
        return masked_number


# print(mask_for_all("Счет 30377212495530283001"))
