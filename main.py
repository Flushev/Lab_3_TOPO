from classes.app import App
from classes.alarm import Alarm
from classes.tune import Tune
import datetime
import os


def get_choice():
    choice = None
    while choice not in [1, 2, 3]:
        print("Ваш выбор: ", end='')
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                raise Exception
        except Exception as e:
            print("Введено недопустимое значение. Попробуйте еще раз")
    return choice


def main_page(app: App):
    os.system('cls')
    print("__Главное меню__")
    print("1. Список будильников")
    print("2. Создать будильник")
    print("3. Удалить будильник")
    choice = get_choice()
    if choice == 1:
        alarm_list(app)


def alarm_list(app: App):
    os.system('cls')
    print("__Список будильников__")
    app.get_alarm_list()
    l = app.alarms.__len__() + 1
    print(f"{l}. Вернуться в главное меню")
    choice = get_choice()


def main():
    app = App()
    main_page(app)


if __name__ == '__main__':
    main()
