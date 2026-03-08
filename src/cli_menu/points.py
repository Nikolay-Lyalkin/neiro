from src.services.points import PointService


def menu_point():
    point = PointService()
    while True:
        print("""Выберите действие, которое хотите совершить с фигурой точка:
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
            while True:
                print("""
                    Выберите варианты работы с файлами:
                    1. Сохранить все фигуры в файл
                    2. Загрузить все фигуры из файла
                    3. Назад
                    """)
                while True:
                    action_with_file = int(input("Выберите действие: "))
                    if action_with_file in [
                        1,
                        2,
                        3,
                    ]:
                        break
                    else:
                        print("Ошибка! Выберите действие 1, 2 или 3: ")
                        continue
                if action_with_file == 1:
                    path = input("Введите наименование файла, в который хотите сохранить данные: ")
                    point.save_to_json(path=path, name_figure="точка")
                elif action_with_file == 2:
                    path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                    point.load_from_json(path)
                elif action_with_file == 3:
                    break
        elif action == 5:
            break
