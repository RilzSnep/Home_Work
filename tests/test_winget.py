from src.widget import dates, mask_phone_numbers, masks_of_cards


def test_dates() -> None:
    assert dates("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_mask_phone_numbers() -> None:
    assert (
        mask_phone_numbers("Мой номер: +79112345678, позвоните мне, пожалуйста.")
        == "Мой номер: +7911234XXXX, позвоните мне, пожалуйста."
    )
    assert (
        mask_phone_numbers("Звоните по телефону +79115556677 или пишите на номер +79118887766.")
        == "Звоните по телефону +7911555XXXX или пишите на номер +7911888XXXX."
    )


def test_masks_of_cards() -> None:
    assert masks_of_cards("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert masks_of_cards("Счет 73654108430135874305") == "Счет **4305"
