from classes.app import App


def main_page():
    print("Главное меню")
    print("1. Список будильников")
    print("2. Создать будильник")
    print("3. Удалить будильник")
    choice = None
    while choice not in [1, 2, 3]:
        print("Ваш выбор: ", end='')
        try:
            choice = int(input())
            if choice not in [1, 2, 3]:
                raise Exception
        except Exception as e:
            print("Введено недопустимое значение. Попробуйте еще раз")


def main():
    app = App()
    main_page()


if __name__ == '__main__':
    main()

