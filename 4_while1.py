"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    print('Как дела?')
    msg = input()
    while msg != 'Хорошо':
        print('Как дела?')
        msg = input()
    print('Вау')

if __name__ == "__main__":
    hello_user()
