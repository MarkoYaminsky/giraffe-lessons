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
    sum_value = 0
    for digit in str(number):
        sum_value += int(digit)
    return sum_value


def contains_digits(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи стрічка містить хоча б одну цифру"""
    for digit in '1234567890':
        if digit in string:
            return True
    return False


def count_symbols(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Кількість шуканих символів в стрічці"""
    counter = 0
    for letter in string:
        if letter == symbol:
            counter += 1
    return counter


def find_symbol(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Індекс першої зустрічі символу. Якщо він не зустрічається, тоді -1"""
    for character in range(len(string)):
        if string[character] == symbol:
            return character
    return -1


def same_nighbours(string: str) -> int:
    """На вхід програмі подається одна звичайна стрічка.
    :return Скільки в цій стрічці разів сусідні збігаються сусідні символи"""
    counter = 0
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            counter += 1
    return counter


def is_palindrome(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи ця стічка є паліндромом"""
    return string == string[::-1]


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
    return len(string), string * 3, string[0], string[:3], string[-3:], string[::-1], string[1:-1]


def swapped_two_halves(string: str) -> str:
    """На вхід програмі подається стрічка, в якої парна кількість символів.
    :return Нова стрічка, де перша і друга половина поміняні місцями"""
    half_len = len(string) // 2
    return string[half_len:] + string[:half_len]
