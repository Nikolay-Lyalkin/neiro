from src.services.circles import CircleService


def menu_circle():
    circle = CircleService()
    while True:
        print("""Выберите действие, которое хотите совершить с фигурой круг:
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
                    circle.save_to_json(path=path, name_figure="круг")
                elif action_with_file == 2:
                    path = input("Введите путь к файлу из которого хотите загрузить данные: ")
                    circle.load_from_json(path)
                elif action_with_file == 3:
                    break
        elif action == 5:
            break
