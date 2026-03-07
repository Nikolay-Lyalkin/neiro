from src.cli_menu.circles import menu_circle
from src.cli_menu.lines import menu_line
from src.cli_menu.ovals import menu_oval
from src.cli_menu.points import menu_point
from src.cli_menu.rectangles import menu_rect
from src.cli_menu.squares import menu_square


def main():
    print("Добрый день!")
    figure = 0
    while figure != 7:
        print("""Вам предложено выбрать одну из фигур с которой хотите работать:
        1. Точка
        2. Квадрат
        3. Линия
        4. Круг
        5. Овал
        6. Прямоугольник
        7. Выход""")
        figure = int(input("Выберите фигуру: "))
        if figure == 1:
            menu_point()
        elif figure == 2:
            menu_square()
        elif figure == 3:
            menu_line()
        elif figure == 4:
            menu_circle()
        elif figure == 5:
            menu_oval()
        elif figure == 6:
            menu_rect()


if __name__ == "__main__":
    main()
