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
    return len(object_list), \
        object_list[-1], \
        object_list[::-1], \
        5 in object_list and 17 in object_list, \
        object_list[1:-1]


def cubes_list(starting_list: list[int]) -> list[int]:
    """На вхід програмі подається список цілих чисел
    :return список з кубів цих чисел"""
    final_list = []
    for element in starting_list:
        final_list.append(element ** 3)
    return final_list


def crossword(amount_of_words: int, symbol_number: int) -> str:
    """На вхід програмі подається кількість слів та номер шуканого символу.
    Потім з консолі подається amount_of_words слів.
    :return слово, утворене з symbol_number-ого символу кожного слова"""
    result = []
    for _ in range(amount_of_words):
        word = input()
        if len(word) > symbol_number - 1:
            result.append(word[symbol_number - 1])
    return ''.join(result)


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
    splitted = ip_address.split('.')
    
    if len(splitted) != 4:
        return False

    for octet in splitted:
        if not 0 <= int(octet) <= 255:
            return False

    return True


def separate_number_by_average_digit_value(number: int) -> str:
    """На вхід програмі подається ціле число.
    :return його, де між кожним символом буде -середнє значення двох сусідніх цифр-

    8714
    return: 8-7.5-7-4-1-2.5-4"""
    converted = str(number)
    final = []
    for i in range(len(converted) - 1):
        average = (int(converted[i]) + int(converted[i + 1])) / 2
        final.extend([converted[i], str(average)])
    final.append(converted[-1])
    return '-'.join(final)


