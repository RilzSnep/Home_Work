from src.masks import account_mask, card_mask

nums_card_input = input("Введите номер карты: ")
print(card_mask(nums_card_input))

nums_check_input = input("Введите номер счета: ")
print(account_mask(nums_check_input))
