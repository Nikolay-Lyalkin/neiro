from src.services.lines import LineService


def menu_line():
    line = LineService()
    while True:
        print("""Выберите действие, которое хотите совершить с фигурой линия:
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
                line.save_to_json(path=path, name_figure="отрезок")
            elif action_with_file == 2:
                path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                line.load_from_json(path)
        elif action == 5:
            break
