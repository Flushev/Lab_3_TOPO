import time

from classes.app import App
from classes.alarm import Alarm
from classes.tune import Tune
import asyncio
import datetime
import os


def get_values_list(end: int) -> [int]:
    lst = []
    for i in range(1, end + 1):
        lst.append(i)
    return lst


def get_choice(values: [int]):
    choice = None
    while choice not in values:
        print("Ваш выбор: ", end='')
        try:
            choice = int(input())
            if choice not in values:
                raise Exception
        except Exception as e:
            print("Введено недопустимое значение. Попробуйте еще раз")
    return choice


async def main_page(app: App):
    os.system('cls')
    print("__Главное меню__\n")
    print("1. Список будильников")
    print("2. Создать будильник")
    print("3. Удалить будильник")
    values = get_values_list(3)
    choice = get_choice(values)
    if choice == 1:
        await alarm_list(app)
    elif choice == 2:
        await create_alarm(app)


async def alarm_list(app: App):
    os.system('cls')
    print("__Список будильников__\n")
    app.get_alarm_list()
    if app.alarms is not None:
        l = app.alarms.__len__() + 1
    else:
        l = 1
    print(f"{l}. Вернуться в главное меню")
    values = get_values_list(l)
    choice = get_choice(values)


async def create_alarm(app: App):
    os.system('cls')
    print("__Добавление будильника__\n")
    print("Выбор рингтона:")
    app.get_tune_list()
    if app.tunes is not None:
        l = app.tunes.__len__() + 1
    else:
        l = 1
    print(f"{l}. Добавить новый рингтон")
    values = get_values_list(l)
    choice = get_choice(values)
    if choice == l:
        await create_tune(app)
    else:
        tune = app.tunes[choice - 1]
        print("Укажите время (часы): ", end='')
        values = get_values_list(24)
        hour = get_choice(values)
        print("Укажите время (минуты): ", end='')
        values = get_values_list(59)
        minute = get_choice(values)
        time_ = datetime.time(hour=hour, minute=minute)
        print("Введите имя будильника: ", end='')
        name = str(input())
        print("Введите описание будильника: ", end='')
        description = str(input())
        print("Сделать будильник активным? (1 - да, 2 - нет): ", end='')
        values = get_values_list(2)
        active = get_choice(values)
        if active == 1:
            is_active = True
        else:
            is_active = False

        alarm = Alarm(
            name=name,
            description=description,
            tune=tune,
            time=time_,
            is_active=is_active
        )

        app.add_alarm(alarm)

        print("Будильник успешно добавлен")
        time.sleep(2)
        await main_page(app)


async def create_tune(app: App):
    os.system('cls')
    print("__Добавление рингтона__\n")
    print("Введите имя рингтона:")
    name = str(input())
    print("Введите путь до файла:")
    path = str(input())
    tune = Tune(
        name=name,
        path=path
    )
    if not tune.check_exist():
        print("Файл не найден. Попробуйте еще раз")
        time.sleep(2)
        del tune
        await create_alarm(app)
    else:
        app.add_tune(tune)
        print("Рингтон успешно добавлен")
        time.sleep(2)
        await create_alarm(app)


async def main():
    app = App()
    await main_page(app)


if __name__ == '__main__':
    asyncio.run(main())
