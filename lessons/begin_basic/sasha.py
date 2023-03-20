def type_of_variable(variable):
    """На вхід програмі подається змінна

    :return Її тип """
    return type(variable)


def print_words_in_row(word1: str, word2: str, word3: str) -> None:
    """На вхід програмі подається 3 слова. Вивести їх всіх в консоль, кожне з нового рядка.
    Важливо зазначити, що варто використовувати функцію print лише 1 раз
    """
    print(word1, word2, word3, sep='\n')


def print_words_in_column(word1: str, word2: str, word3: str) -> None:
    """На вхід програмі подається 3 слова. Вивести їх всіх в консоль, в одному рядку, через кому.
    Важливо зазначити, що варто використати функцію print 3 рази.
    """
    print(word1, end=' , ')
    print(word2, end=' , ')
    print(word3)


def string_multiplication(quantity: int) -> str:
    """Користувач зчитує з клавіатури певну стрічку.
    На вхід програмі подається множник стрічки.

    :return (Множник) разів повторену стрічку"""
    some_word = input()
    return some_word * quantity


def multiplication_of_input_numbers() -> int:
    """На вхід програмі нічого не подається.
    Після запуску функції користувач почергово вводить в термінал 2 числа.

    :return Добуток зчитаних чисел
    """
    first_number = int(input())
    second_number = int(input())
    return first_number * second_number


def all_operations_in_one(number1: int, number2: int) -> int or float:
    """На вхід програмі подається 2 цілих числа. Друге - не нуль.

    Вивести всі можливі математичні операції між ними
    (сума, різниця, добуток, ділення, ділення націло, отримання остачі, піднесення в степінь)
    в одному рядку через кому
    """
    print(number1 + number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1 / number2)
    print(number1 // number2)
    print(number1 % number2)
    print(number1 ** number2)


def only_positive(number1: int, number2: int, number3: int) -> int:
    """На вхід програмі подається 3 цілих числа.

    :return Сума тільки тих з них, які мають додатне значення"""
    summa = 0
    if number1 > 0:
        summa += number1
    if number2 > 0:
        summa += number2
    if number3 > 0:
        summa += number3
    return summa


def beyond_two(lower_limit: int, upper_limit: int, number: int) -> bool:
    """На вхід програмі подається два цілі числа - нижня і верхням межа відрізка.

    :return Чи число лежить на відрізку"""
    return lower_limit < number < upper_limit


def pretty_number(questionable_number: int) -> bool:
    """На вхід програмі подається ціле число.
    Число можна вважати красивим, якщо воно ділиться націло на 7 або на 17, а також має 4 цифри.

    :return Чи число є красивим"""
    return questionable_number % 7 == 0 or questionable_number % 17 == 0 and 999 < questionable_number < 10000


def calculator(number1: int or float, number2: int or float, operator: str):
    """На вхід програмі подається 2 числа, а потім оператор.

    :return Результат операції першого числа з другим.
    * Врахувати, що ділити на 0 не можна"""


def rook_move(x1: int, y1: int, x2: int, y2: int):
    """На вхід програмі подається 4 числа, координати шахової фігури тури до і після ходу.
    Тура може ходити лише по горизонталі та по вертикалі на шаховій дошці.
    Умову того, що координати мають обмежуватися число 8, можна опустити
    :return чи може тура за один хід здійснити переміщення з (x1, y1) в (x2, y2)
    """
