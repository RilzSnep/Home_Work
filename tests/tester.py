from src.widget import datetime_and_date, masks_of_cards

cards_input = input("Введите номер карты/счета:")
print(masks_of_cards(cards_input))
data_input = input("Введите дату:")
print(datetime_and_date(data_input))
