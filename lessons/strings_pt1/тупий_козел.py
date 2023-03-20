def even_indices(string: str) -> str:
    """На вхід програмі подається одна звичайна стрічка.
    :return Нова стрічка, де буде присутній кожен символ з парним індексом, розділений \n (0 теж парний)"""
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i] + '\n'
    return new_string  # костилі


def reversed_string(string: str) -> str:
    """На вхід програмі подається одна звичайна стрічка.
    :return Нова стрічка, в якій символи стоять у зворотному порядку"""
    final_string = ''
    for i in range(len(string) - 1, -1, -1):
        final_string += string[i]
    return final_string


def initials(name: str, surname: str, father_name: str) -> str:
    """На вхід програмі подаються імʼя та прізвище людини, а також як звати її батька
    :return Нова стрічка, яка буде складатися з абревіатури цих слів, де після кожної букви стоятиме крапка"""
    return f'{name[0]}.{surname[0]}.{father_name[0]}'


def summ_of_digits(number: int) -> int:
    """На вхід програмі подається число.
    :return Сума його цифр"""
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    return digit_sum


def contains_digits(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи стрічка містить хоча б одну цифру"""
    for digit in range(10):
        if str(digit) in string:
            return True
    return False
# маєш плюсик за гарне рішення


def count_symbols(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Кількість шуканих символів в стрічці"""
    counter = 0
    for i in string:
        if i == symbol:
            counter += 1
    return counter


def find_symbol(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Індекс першої зустрічі символу. Якщо він не зустрічається, тоді -1"""
    for i in range(len(string)):
        if string[i] == symbol:
            return i
    return -1


def same_nighbours(string: str) -> int:
    """На вхід програмі подається одна звичайна стрічка.
    :return Скільки в цій стрічці разів збігаються сусідні символи"""
    counter = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
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
    mult_string = string * 3
    first_three_symbols = string[:3]
    last_three_symbols = string[-3:]  # ??? костиль!
    reverse = reversed_string(string)
    circumcised_string = string[1:-1]
    return len(string), mult_string, string[0], first_three_symbols, last_three_symbols, reverse, circumcised_string


def swapped_two_halves(string: str) -> str:
    """На вхід програмі подається стрічка, в якої парна кількість символів.
    :return Нова стрічка, де перша і друга половина поміняні місцями"""
    first_half = string[:len(string) // 2]  # не спрацює )))) )))) )))) ))))
    second_half = string[-(len(string) // 2):]  # спрацювало (((( (((( (((( ((((
    return second_half + first_half
