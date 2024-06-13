from typing import Any
from src.filter_descripions import filter_transactions_by_description
from src.csv_and_xlsx import read_csv, read_xlsx
from src.generators import filter_by_currency_csv, filter_by_currency_pop
from src.masks import mask_for_all
from src.processing import filter_by_state, sort_by_data
from src.utils import load_transactions
from src.widget import dates

print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.\n Выберите необходимый пункт меню:")
print("1. Получить информацию о транзакциях из json файла")
print("2. Получить информацию о транзакциях из csv файла")
print("3. Получить информацию о транзакциях из xlsx файла")
user_answer_1 = input()


def check_answer_1(user_answer: Any) -> Any:
    """
    Проверяет введенный пользователем ответ на первый вопрос и переводят их в int.
    """
    while user_answer not in ("1", "2", "3"):
        user_answer = input("Нет такого варианта ответа, попробуйте снова(1, 2, 3): ")
        user_answer = user_answer
    user_answer = int(user_answer)
    print(f"Вы выбрали пункт {user_answer}")


def for_answer_2() -> Any:
    """
    функия для считывания json, csv , xlsx файлов
    """
    if user_answer_1 == "1":
        transactions = load_transactions("data/operations.json")
    elif user_answer_1 == "2":
        transactions = read_csv("data/transactions.csv")
    else:
        transactions = read_xlsx("data/transactions_excel.xlsx")
    user_answer_2 = input("Введите статус транзакции (EXECUTED, CANCELED, PENDING): ").upper()
    while user_answer_2 not in ("EXECUTED", "CANCELED", "PENDING"):
        user_answer_2 = input("Вы ввели некорректный статус транзакции, попробуйте снова(EXECUTED, CANCELED, PENDING): ")
        user_answer_2 = user_answer_2.upper()
    print(f"Операции отфильтрованы по статусу {user_answer_2}")
    transactions_status = filter_by_state(transactions, user_answer_2)
    return transactions_status


def for_answers_3_4(transactions_status: Any) -> Any:
    """
    Сортировка по дате
    """
    user_answer_3 = input("Отсортировать операции по дате? Да/Нет \n").upper()
    while user_answer_3 not in ("НЕТ", "ДА"):
        user_answer_3 = input("Нет такого варианта ответа, попробуйте снова (Да/Нет): ")
        user_answer_3 = user_answer_3.upper()
    if user_answer_3 == "ДА":
        user_answer_4 = input("Отсортировать по \n1-возрастанию \n2-убыванию?\n")
        while user_answer_4 not in ("1", "2"):
            user_answer_4 = input("Нет такого варианта ответа, попробуйте снова \n1-возрастанию \n2-убыванию?\n")
            user_answer_4 = user_answer_4
        if user_answer_3 == "ДА":
            if user_answer_4 == "1":
                transactions_status = sort_by_data(transactions_status, rever=False)
            else:
                transactions_status = sort_by_data(transactions_status)
            print("Операции отсортированы по дате")
    return transactions_status


def for_answer_5(user_answer: Any, transactions_status: Any) -> Any:
    """
    Сортировка по руб. транзакциям
    """
    user_answer_5 = input("Выводить только рублевые тразакции? Да/Нет\n").upper()
    while user_answer_5 not in ("НЕТ", "ДА"):
        user_answer_5 = input("Нет такого варианта ответа, попробуйте снова (Да/Нет):")
        user_answer_5 = user_answer_5.upper()

    if user_answer_5 == "ДА" and user_answer != "1":
        transactions_status = filter_by_currency_csv(transactions_status)
        print("Операции отфильтрованы по рублевым транзакциям\n")
    elif user_answer_5 == "ДА" and user_answer == "1":
        transactions_status = filter_by_currency_pop(transactions_status)
        print("Операции отфильтрованы по рублевым транзакциям\n")

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions_status)}")
    if user_answer == "1":
        for i in transactions_status:
            if i["description"] == "Открытие вклада":
                print(dates(i["date"]), i["description"])
                print(mask_for_all(i["to"]))
                print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['code']}\n")
            else:
                print(dates(i["date"]), i["description"])
                print(f"{mask_for_all(i['from'])}  ->  {mask_for_all(i['to'])}")
                print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['code']}\n")

    elif user_answer == "2" or user_answer == "3":
        for i in transactions_status:
            if i["description"] == "Открытие вклада":
                print(dates(i["date"]), i["description"])
                print(mask_for_all(i["to"]))
                print(f"Сумма: {i['amount']} {i['currency_code']}\n")
            else:
                print(dates(i["date"]), i["description"])
                print(f"{mask_for_all(i['from'])}  ->  {mask_for_all(i['to'])}")
                print(f"Сумма: {i['amount']} {i['currency_code']}\n")


def main() -> None:
    check_answer_1(user_answer_1)
    data = for_answer_2()
    data = for_answers_3_4(data)
    data = filter_transactions_by_description(data)
    for_answer_5(user_answer_1, data)


main()
