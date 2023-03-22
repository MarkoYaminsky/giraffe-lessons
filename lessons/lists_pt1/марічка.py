def create_list_to_(limit: int) -> list[int]:
    """На вхід програмі подається число - межа.
    :return список чисел від 0 до limit включно"""
    return list(range(limit + 1))


def get_list_info(object_list: list[int]) -> tuple:
    """На вхід програмі подається список чисел
    :return
    - довжина списка
    - останній елемент списка
    - список у зворотному порядку
    - чи список містить числа 5 та 17
    - той самий список, з видаленим першим та останнім елементом"""
    return len(object_list), object_list[-1], object_list[::-1], 5 in object_list and 17 in object_list, object_list[1:-1]


def cubes_list(starting_list: list[int]) -> list[int]:
    """На вхід програмі подається список цілих чисел
    :return список з кубів цих чисел"""
    return [x**3 for x in starting_list]


def crossword(amount_of_words: int, symbol_number: int) -> str:
    """На вхід програмі подається кількість слів та номер шуканого символу.
    Потім з консолі подається amount_of_words слів.
    :return слово, утворене з symbol_number-ого символу кожного слова"""
    word_to_return = []
    for i in range(amount_of_words):
        word = input()
        word_to_return += word[symbol_number]
    return ''.join(word_to_return)


def list_from_string(string: str) -> list[str]:
    """На вхід програмі подається речення
    :return список з його слів"""
    return string.split()


def initials_2(path_components: list[str]) -> str:
    """На вхід програмі подається повний шлях до програми, де одна ланка - один елемент списку
    :return зʼєднаний шлях до програми (за сепаратор можна брати передній слеш /)"""
    return '/'.join(path_components)


def ip_address_is_correct(ip_address: str) -> bool:
    """На вхід програмі подається ip-адреса.
    Вона є валідною, якщо кожен октет в межах від 0 до 255 влючно, а також є рівно 4 октети
    :return чи ip-адреса валідна"""
    oct_count = 0
    for octet in ip_address.split('.'):
        oct_count += 1
        if int(octet) > 255:
            return False
    return oct_count == 4


def separate_number_by_average_digit_value(number: int) -> str:
    """На вхід програмі подається ціле число.
    :return його, де між кожним символом буде -середнє значення двох сусідніх цифр-

    8714
    return: 8-7.5-7-4.0-1-2.5-4"""
    string = str(number)
    my_list = [int(x) for x in string]
    list_to_return = [string[0]]
    for i in range(len(my_list) - 1):
        average = (my_list[i] + my_list[i + 1]) / 2
        list_to_return.append(f'-{average}-')
        list_to_return.append(str(my_list[i + 1]))
    print(''.join(list_to_return))


'''def separate_number_by_average_digit_value_original(number: int) -> str:
    """На вхід програмі подається ціле число.
    :return його, де між кожним символом буде -середнє значення цифр числа-

    8714
    return: 8-5-7-5-1-5-4
    """
    numbers_list = []
    sum_value = 0
    for digit in str(number):
        sum_value += int(digit)
        numbers_list.append(digit)
    average = sum_value // len(numbers_list)
    return f'-{average}-'.join(numbers_list)
'''