from src.widget import datetime_to_date, masks_of_cards

cards_input = input("Введите номер карты/счета:")
print(masks_of_cards(cards_input))
data_input = input("Введите дату:")
print(datetime_to_date(data_input))
