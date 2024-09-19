"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime

today = datetime.datetime.today().day()
yesterday = today - datetime.timedelta(days=1)
thirty_days_ago = today - datetime.timedelta(days=30)

def print_days():
    print("Сегодняшняя дата: ", today)
    print("Вчерашняя дата: ", yesterday)
    print("Дата 30 дней назад: ", thirty_days_ago)


def str_2_datetime(date_string):
    return datetime.datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
  

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
