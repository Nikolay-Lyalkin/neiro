from src.services.circles import CircleService
from src.services.lines import LineService
from src.services.points import PointService
from src.services.squares import SquareService


def main():
    print("Добрый день!")
    figure = 0
    while figure != 5:
        print("""Вам предложено выбрать одну из фигур с которой хотите работать:
        1. Точка
        2. Квадрат
        3. Линия
        4. Круг
        5. Выход""")
        figure = int(input("Выберите фигуру: "))
        if figure == 1:
            point = PointService()
            print("""Выберите действие, которое хотите совершить с фигурой:
            1. Создать
            2. Посмотреть все фигуры
            3. Удалить
            4. Назад""")

            while True:
                action = int(input("Выберите действие: "))
                if action in [1, 2, 3, 4]:
                    break
                else:
                    print("Ошибка! Выберите действие от 1 до 4: ")
                    continue

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
                continue
        elif figure == 2:
            square = SquareService()
            print("""Выберите действие, которое хотите совершить с фигурой:
            1. Создать
            2. Посмотреть все фигуры
            3. Удалить
            4. Назад""")

            while True:
                action = int(input("Выберите действие: "))
                if action in [1, 2, 3, 4]:
                    break
                else:
                    print("Ошибка! Выберите действие от 1 до 4: ")
                    continue

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
                continue
        elif figure == 3:
            line = LineService()
            print("""Выберите действие, которое хотите совершить с фигурой:
                1. Создать
                2. Посмотреть все фигуры
                3. Удалить
                4. Назад""")

            while True:
                action = int(input("Выберите действие: "))
                if action in [1, 2, 3, 4]:
                    break
                else:
                    print("Ошибка! Выберите действие от 1 до 4: ")
                    continue

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
                continue
        elif figure == 4:
            circle = CircleService()
            print("""Выберите действие, которое хотите совершить с фигурой:
                    1. Создать
                    2. Посмотреть все фигуры
                    3. Удалить
                    4. Назад""")

            while True:
                action = int(input("Выберите действие: "))
                if action in [1, 2, 3, 4]:
                    break
                else:
                    print("Ошибка! Выберите действие от 1 до 4: ")
                    continue

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
                continue


if __name__ == "__main__":
    main()
