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
    number_in_str = str(number)
    number_lenght = len(number_in_str)
    summ = 0
    for i in range(number_lenght):
        summ += int(number[i])
    return summ


def contains_digits(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи стрічка містить хоча б одну цифру"""
    number = "1234567890"
    for letter in string:
        if letter in number:
            return True
    return False


def count_symbols(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Кількість шуканих символів в стрічці"""
    count = 0
    for _ in string:
        if _ == symbol:
            count += 1
    return count


def find_symbol(string: str, symbol: str) -> int:
    """На вхід програмі подається одна звичайна стрічка, а також шуканий символ.
    :return Індекс першої зустрічі символу. Якщо він не зустрічається, тоді -1"""
    for i in range(len(string)):
        if string[i] == symbol:
            return i
    return -1


def same_nighbours(string: str) -> int:
    """На вхід програмі подається одна звичайна стрічка.
    :return Скільки в цій стрічці разів сусідні збігаються сусідні символи"""
    summ = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            summ += 1
    return summ


def is_palindrome(string: str) -> bool:
    """На вхід програмі подається одна звичайна стрічка.
    :return Чи ця стічка є паліндромом"""
    reversed_string = string[::-1]
    return reversed_string == string


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
    return len(string), \
           string * 3, \
           string[0], \
           string[:3], \
           string[- 3:], \
           string[::-1], \
           string[1:-1]


def swapped_two_halves(string: str) -> str:
    """На вхід програмі подається стрічка, в якої парна кількість символів.
    :return Нова стрічка, де перша і друга половина поміняні місцями"""
    string_1 = string[: len(string)//2]
    string_2 = string[len(string)//2: ]
    return string_2+ string_1
