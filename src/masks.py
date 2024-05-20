from src.logger import logger_setup

logger = logger_setup()


def account_mask(num_account: str) -> str:
    """Получает номер счета и выводит его под маской"""
    if len(num_account) == 16:
        mask_account = num_account[-4:]
        logger.info("Account was mask")
        return f"**{mask_account}"
    else:
        logger.error("Account was not mask")
        return num_account


def card_mask(cards_mask: str) -> str:
    """Получает номер карты и выводит его под маской"""
    if len(cards_mask) == 21:
        mask_card = f"{cards_mask[:4]} {cards_mask[4:6]}** **** {cards_mask[-4:]}"
        logger.info("Card was mask")
        return mask_card
    else:
        logger.error("Card was not mask")
        return cards_mask


account_mask("1234567890123456")
card_mask("12345678901234567890123456789012")
