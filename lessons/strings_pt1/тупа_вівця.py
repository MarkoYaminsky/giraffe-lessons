def even_indices(string: str) -> str:
    """На вхід програмі подається одна звичайна стрічка.
    :return Нова стрічка, де буде присутній кожен символ з парним індексом, розділений \n (0 теж парний)"""
    final_string = ''
    for index in range(0, len(string), 2):
        final_string += string[index] + '\n'
    return final_string

def reversed_string(string: str) -> str:
    """На вхід програмі подається одна звичайна стрічка.
    :return Нова стрічка, в якій символи стоять у зворотному порядку"""
    reversed_string_value = ''
    for index in range(len(string) - 1, -1, -1):
        reversed_string_value += string[index]
    return reversed_string_value


def initials(name: str, surname: str, father_name: str) -> str:
    """На вхід програмі подаються імʼя та прізвище людини, а також як звати її батька
    :return Нова стрічка, яка буде складатися з абревіатури цих слів, де після кожної букви стоятиме крапка"""
    return f'{name[0]}.{surname[0]}.{father_name[0]}.'


def summ_of_digits(number: int) -> int:
    """На вхід програмі подається число.
    :return Сума його цифр"""

    # створити змінну з сумою
    string_number = str(number)
    for digit in string_number:
        summ +=  # додавати в свою змінну з сумою числове значення поточного символу
    return summ  # повернути суму


def contains_digits(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи стрічка містить хоча б одну цифру"""


def count_symbols(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Кількість шуканих символів в стрічці"""


def find_symbol(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Індекс першої зустрічі символу. Якщо він не зустрічається, тоді -1"""


def same_nighbours(string: str) -> int:
    """На вхід програмі подається одна звичайна стрічка.
    :return Скільки в цій стрічці разів сусідні збігаються сусідні символи"""


def is_palindrome(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи ця стічка є паліндромом"""


def slices_1(string: str) -> tuple:
    """На вхід програмі подається одна звичайна стрічка.
    :return
    - загальна кількість символів у стрічці;
    - вхідну стрічку, повторену 3 рази;
    - перший символ стрічки;
    - перші три символи стрічки;
    - останні три символи стрічки;
    - стрічку у зворотному порядку;
    - стрічку з видаленим першим та останнім символом.

    Всі ці значення потрібно перелічити через кому при поверненні з функції"""


def swapped_two_halves(string: str) -> str:
    """На вхід програмі подається стрічка, в якої парна кількість символів.
    :return Нова стрічка, де перша і друга половина поміняні місцями"""
