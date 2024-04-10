from src.widget import datetime_and_date, mask_phone_numbers, masks_of_cards

cards_input = input("Введите номер карты/счета:")
print(masks_of_cards(cards_input))
data_input = input("Введите дату:")
print(datetime_and_date(data_input))
input_texts = input("Как с вами связаться? :")
masked_text = mask_phone_numbers(input_texts)
print(masked_text)
