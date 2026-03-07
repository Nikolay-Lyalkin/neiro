from src.cli_menu.ovals import oval_menu
from src.services.circles import CircleService
from src.services.lines import LineService
from src.services.points import PointService
from src.services.squares import SquareService


def main():
    print("Добрый день!")
    figure = 0
    while figure != 6:
        print("""Вам предложено выбрать одну из фигур с которой хотите работать:
        1. Точка
        2. Квадрат
        3. Линия
        4. Круг
        5. Овал
        6. Выход""")
        figure = int(input("Выберите фигуру: "))
        if figure == 1:

            while True:
                point = PointService()
                print("""Выберите действие, которое хотите совершить с фигурой:
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
                        print(f"Выберите целое число от 1 до 5")

                if action == 1:
                    while True:
                        try:
                            x = int(input("Введите координату Х: "))
                            y = int(input("Введите координату Y: "))
                            break
                        except ValueError:
                            print("Ошибка! X и Y должны быть целыми числами.")
                    point.create(x, y)
                elif action == 2:
                    point.show_figures()
                elif action == 3:
                    while True:
                        try:
                            id_figure = int(input("Введите индекс фигуры, которую хотите удалить: "))
                            break
                        except ValueError:
                            print("Ошибка! ID должен быть целыми числом.")
                    point.delete(id_figure)
                elif action == 4:
                    print(f"""
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
                        point.save_to_json(path=path, name_figure="точка")
                    elif action_with_file == 2:
                        path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                        point.load_from_json(path)
                elif action == 5:
                    break
        elif figure == 2:
            while True:
                square = SquareService()
                print("""Выберите действие, которое хотите совершить с фигурой:
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
                        print(f"Выберите целое число от 1 до 5")

                if action == 1:
                    while True:
                        try:
                            x_left_up = int(input("Введите координату Х левого верхнего угла: "))
                            y_left_up = int(input("Введите координату Y левого верхнего угла: "))
                            x_left_down = int(input("Введите координату Х левого верхнего угла: "))
                            y_left_down = int(input("Введите координату Y левого верхнего угла: "))
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
                    print(f"""
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
        elif figure == 3:
            while True:
                line = LineService()
                print("""Выберите действие, которое хотите совершить с фигурой:
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
                            x_left = int(input("Введите координату Х начала отрезка: "))
                            y_left = int(input("Введите координату Y начала отрезка: "))
                            x_right = int(input("Введите координату Х конца отрезка: "))
                            y_right = int(input("Введите координату Y конца отрезка: "))
                            length = int(input("Введите длину отрезка: "))
                            break
                        except ValueError:
                            print("Ошибка! X и Y должны быть целыми числами.")
                    line.create(x_left, y_left, x_right, y_right, length)
                elif action == 2:
                    line.show_figures()
                elif action == 3:
                    while True:
                        try:
                            id_figure = int(input("Введите индекс фигуры, которую хотите удалить: "))
                            break
                        except ValueError:
                            print("Ошибка! ID должен быть целыми числом.")
                    line.delete(id_figure)
                elif action == 4:
                    print(f"""
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
                        line.save_to_json(path=path, name_figure="отрезок")
                    elif action_with_file == 2:
                        path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                        line.load_from_json(path)
                elif action == 5:
                    break
        elif figure == 4:
            circle = CircleService()
            while True:
                print("""Выберите действие, которое хотите совершить с фигурой:
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
                            x = int(input("Введите координату Х центра круга: "))
                            y = int(input("Введите координату Y центра круга: "))
                            radius = int(input("Введите радиус круга: "))
                            circle.create(x, y, radius)
                            break
                        except ValueError:
                            print(
                                "Ошибка! X и Y должны быть целыми числами, радиус не может быть равен 0 или"
                                "или быть отрицательным числом."
                            )
                elif action == 2:
                    circle.show_figures()
                elif action == 3:
                    while True:
                        try:
                            id_figure = int(input("Введите индекс фигуры, которую хотите удалить: "))
                            break
                        except ValueError:
                            print("Ошибка! ID должен быть целыми числом.")
                    circle.delete(id_figure)
                elif action == 4:
                    print(f"""
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
                        circle.save_to_json(path=path, name_figure="круг")
                    elif action_with_file == 2:
                        path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                        circle.load_from_json(path)
                elif action == 5:
                    break
        elif figure == 5:
            oval_menu()


if __name__ == "__main__":
    main()
