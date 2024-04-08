def account_mask(num_account: str) -> str:
    """Получает номер счета и выводит его под маской"""
    mask_account = num_account[-4:]
    return f"**{mask_account}"


def card_mask(cards_mask: str) -> str:
    """Получает номер карты и выводит его под маской"""
    mask_card = f"{cards_mask[:4]} {cards_mask[4:6]}** **** {cards_mask[-4:]}"
    return mask_card
