from src.services.squares import SquareService


def menu_square():
    square = SquareService()
    while True:
        print("""Выберите действие, которое хотите совершить с фигурой квадрат:
                    1. Создать
                    2. Посмотреть все фигуры
                    3. Удалить
                    4. Работа с файлами
                    5. Назад""")

        while True:
            try:
                action = int(input("Выберите действие: "))
                if action in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Ошибка! Выберите действие от 1 до 5: ")
                    continue
            except ValueError:
                print("Выберите целое число от 1 до 5")

        if action == 1:
            while True:
                try:
                    x_left_up = int(input("Введите координату Х левого верхнего угла: "))
                    y_left_up = int(input("Введите координату Y левого верхнего угла: "))
                    x_left_down = int(input("Введите координату Х левого нижнего угла: "))
                    y_left_down = int(input("Введите координату Y левого нижнего угла: "))
                    side = int(input("Введите длину стороны квадрата: "))
                    square.create(x_left_up, y_left_up, x_left_down, y_left_down, side)
                    break
                except ValueError:
                    print(
                        "Ошибка! X и Y должны быть целыми числами, сторона не может быть равна 0 или "
                        "быть отрицательным числом."
                    )
        elif action == 2:
            square.show_figures()
        elif action == 3:
            while True:
                try:
                    id_figure = int(input("Введите индекс фигуры, которую хотите удалить: "))
                    break
                except ValueError:
                    print("Ошибка! ID должен быть целыми числом.")
            square.delete(id_figure)
        elif action == 4:
            print("""
                        Выберите варианты работы с файлами:
                        1. Сохранить все фигуры в файл
                        2. Загрузить все фигуры из файла
                        """)
            while True:
                action_with_file = int(input("Выберите действие: "))
                if action_with_file in [
                    1,
                    2,
                ]:
                    break
                else:
                    print("Ошибка! Выберите действие 1 или 2: ")
                    continue
            if action_with_file == 1:
                path = input("Введите наименование файла, в который хотите сохранить данные: ")
                square.save_to_json(path=path, name_figure="квадрат")
            elif action_with_file == 2:
                path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                square.load_from_json(path)
        elif action == 5:
            break
