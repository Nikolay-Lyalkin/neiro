from src.services.ovals import OvalService


def menu_oval():
    oval = OvalService()
    while True:
        print("""Выберите действие, которое хотите совершить с фигурой овал:
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
                    x_center = int(input("Введите координату Х центра овала: "))
                    y_center = int(input("Введите координату Y центра овала: "))
                    x_radius = int(input("Введите  координату Х радиуса овала: "))
                    y_radius = int(input("Введите  координату Y радиуса овала: "))
                    oval.create(x_center, y_center, x_radius, y_radius)
                    break
                except ValueError:
                    print(
                        "Ошибка! X и Y центра овала должны быть целыми числами,"
                        "X и Y радиуса овала должны быть целыми положительными числами."
                    )
        elif action == 2:
            oval.show_figures()
        elif action == 3:
            while True:
                try:
                    id_figure = int(input("Введите индекс фигуры, которую хотите удалить: "))
                    break
                except ValueError:
                    print("Ошибка! ID должен быть целыми числом.")
            oval.delete(id_figure)
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
                    oval.save_to_json(path=path, name_figure="овал")
                elif action_with_file == 2:
                    path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                    oval.load_from_json(path)
                elif action_with_file == 3:
                    break
        elif action == 5:
            break
