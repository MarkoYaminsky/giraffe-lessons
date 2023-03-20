def even_indices(string: str) -> str:
    """На вхід програмі подається одна звичайна стрічка.
    :return Нова стрічка, де буде присутній кожен символ з парним індексом, розділений \n (0 теж парний)"""
    final_string = ''
    for index in range(len(string)):
        if index % 2 == 0:
            final_string = string[index] + '\n'
    return final_string


def reversed_string(string: str) -> str:
    """На вхід програмі подається одна звичайна стрічка.
    :return Нова стрічка, в якій символи стоять у зворотному порядку"""
    new_string = ''
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    return new_string


def initials(name: str, surname: str, father_name: str) -> str:
    """На вхід програмі подаються імʼя та прізвище людини, а також як звати її батька
    :return Нова стрічка, яка буде складатися з абревіатури цих слів, де після кожної букви стоятиме крапка"""
    return f'{name[0]}. {surname[0]}. {father_name[0]}.'


def summ_of_digits(number: int) -> int:
    """На вхід програмі подається число.
    :return Сума його цифр"""
    digits_sum = 0
    final_number = str(number)
    for digit in final_number:
        digits_sum += int(digit)
    return digits_sum


def contains_digits(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи стрічка містить хоча б одну цифру"""
    all_digits = '0123456789'
    for symbol in string:
        if symbol in all_digits:
            return True
    return False


def count_symbols(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Кількість шуканих символів в стрічці"""
    count = 0
    for char in string:
        if char == symbol:
            count += 1
    return count


def find_symbol(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Індекс першої зустрічі символу. Якщо він не зустрічається, тоді -1"""
    for index in range(len(string)):
        if symbol == string[index]:
            return index
        else:
            return -1


def same_nighbours(string: str) -> int:
    """На вхід програмі подається одна звичайна стрічка.
    :return Скільки в цій стрічці разів сусідні збігаються сусідні символи"""
    count = 0
    for index in range(len(string - 1)):
        if string[index] == string[index + 1]:
            count += 1
    return count


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
