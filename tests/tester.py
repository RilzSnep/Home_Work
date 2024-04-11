from src.widget import dates, mask_phone_numbers, masks_of_cards

cards_number_input = input("Введите номер карты/счета:")
print(masks_of_cards(cards_number_input))
data_input = input("Введите дату:")
print(dates(data_input))
input_texts = input("Как с вами связаться? :")
masked_text = mask_phone_numbers(input_texts)
print(masked_text)
