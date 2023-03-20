def python_is_awesome() -> None:
    """На вхід програмі нічого не подається.
    Вивести фразу 'python is awesome!' за допомогою функції print 10 разів"""
    for i in range(10):
        print('python is awesome!')


def something_is_awesome(word: str, count: int) -> None:
    """На вхід програмi подається якесь слово та змінна count.
    Вивести фразу '(слово) is awesome!' за допомогою функції print count разів"""
    for i in range(count):
        print(word + ' is awesome')


def enumerate_rows(phrase: str, row_count: int) -> None:
    """На вхід програмі подається фраза та кількість її повторень.
    Вивести цю фразу row_count разів з індексом починаючи від нуля

    (наприклад, "Саша - Маша", 5)
    0 Саша - Маша
    1 Саша - Маша
    2 Саша - Маша
    3 Саша - Маша
    4 Саша - Маша
    """
    for i in range(row_count):
        print(i, phrase)


def range_included(count: int) -> range:
    """На вхід проагрмі подається ціле число count.
    :return всі числа від 0 до count включно"""
    return range(count + 1)


def intelligent_range(point1, point2) -> range:
    """На вхід програмі подається 2 числа.
    Якщо число 1 (нехай, m) менше за число 2 (нехай, n), тоді повернути всі числа від m до n включно
    Якщо ж число 1 m більше за n, тоді повернути всі числа від m до n включно в порядку спадання
    Припустимо, що m != n

    :return згідно з умовою"""
    if point1 < point2:
        return range(point1, point2 + 1)
    else:
        return range(point1, point2 - 1, -1)  # point2 не включається в твоєму коді


def dividers(number: int) -> None:
    """На вхід програмі подається число.
    Вивести всі його дільники, окрім 1 та його самого"""
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            print(i)


def counting_4_9(lower_limit: int, upper_limit: int) -> int:
    """На вхід програмі подається два числа, перше менше за друге.
    :return кількість чисел, що закінчуються на 4 або 9

    Підказка: Щоб знайти останню цифру числа, можна скористатися діленням по модулю ;)"""
    counter = 0
    for number in range(lower_limit, upper_limit):
        if number % 10 == 4 or number % 10 == 9:
            counter += 1
    return counter


def factorial(number: int) -> int:
    """На вхід програмі подається ціле число.
    :return його факторіал"""
    # import math
    # return math.factorial(number) ?
    if number == 0:
        return 1
    elif number > 0:
        return number * factorial(number - 1)  # верес мене з'їсть за рекурсію


def only_even(count_of_numbers: int) -> bool:
    """На вхід програмі подається кількість чисел, а потім самі числа з консолі.
    :return чи всі з них парні"""

    # is_even = True
    # for i in range(count_of_numbers):
    #     number = int(input())
    #     if number % 2 != 0:
    #         is_even = False
    # return is_even

    return all([True if i % 2 == 0 else False for i in [int(input()) for _ in range(count_of_numbers)]])

