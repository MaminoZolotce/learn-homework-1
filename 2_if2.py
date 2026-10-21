"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main(message1, message2):
    if isinstance(message1, str) and isinstance(message2, str):
        if message1 == message2:
            return 1
        elif len(message1) > len(message2):
            return 2
        elif message1 != message2 and message2 == "learn":
            return 3

    return 0

if __name__ == "__main__":
    for i in range(0,3):
        message1 = input()
        message2 = input()
        func1 = main(message1, message2)
        print(func1)
