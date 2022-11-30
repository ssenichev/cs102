import typing as tp
from math import cos, log, log10, sin, tan


def calc_2(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    """
    mathematical operations
    """
    if command == "+":
        return num_1 + num_2
    if command == "-":
        return num_1 - num_2
    if command == "/":
        return num_1 / num_2
    if command == "*":
        return num_1 * num_2
    if command == "^":
        if num_1 < 0 and num_2 < 1 and num_2 % 2 == 0:
            return "Невозможно вычислить"
        else:
            return num_1**num_2
    else:
        return f"Неизвестный оператор: {command!r}."


def calc_1(num_1: float, command: str) -> tp.Union[float, str]:  # type: ignore
    """
    mathematical functions
    """
    if command == "^2":
        return num_1**2
    if command == "sin":
        return sin(num_1)
    if command == "cos":
        return cos(num_1)
    if command == "tan":
        return tan(num_1)
    if command == "ln":
        if num_1 <= 0:
            return "Невозможно"
        return log(num_1)
    if command == "lg":
        if num_1 <= 0:
            return "Невозможно"
        return log10(num_1)


def numeral_system(num_1: int, num_2: int, command: str) -> tp.Union[int, str]:
    """
    changing the numeral system
    """
    empty_str = ""
    if num_1 < 0:
        return "Нельзя конвертировать отрицательное число"
    if num_2 > 9 or num_2 < 2:
        return "Выберите с. с. больше 2 и меньше 10"
    if command == "convert":
        if num_1 == 0:
            return 0
        while num_1 > 0:
            empty_str = empty_str + str(num_1 % num_2)
            num_1 //= num_2
    return empty_str[::-1]


if __name__ == "__main__":
    while True:
        try:
            COMMAND = input("Введите операцию > ")
            if COMMAND.isdigit() and int(COMMAND) == 0:
                break
            if COMMAND in ("+", "-", "/", "*", "^"):
                NUM_1 = float(input("Первое число > "))
                NUM_2 = float(input("Второе число > "))
                print(calc_2(NUM_1, NUM_2, COMMAND))
            elif COMMAND in ("^2", "cos", "sin", "tan", "ln", "lg"):
                NUM_1 = float(input("Введите число > "))
                print(calc_1(NUM_1, COMMAND))
            elif COMMAND == "convert":
                NUM_1 = int(input("Первое число > "))
                NUM_2 = int(input("Второе число > "))
                print(numeral_system(NUM_1, NUM_2, COMMAND))
            else:
                print("Be careful! Try again")
        except ValueError:
            print("Ошибка! Вы ввели не число. Try again!")
