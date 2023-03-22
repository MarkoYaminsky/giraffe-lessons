def create_list_to_(limit: int) -> list[int]:
    """На вхід програмі подається число - межа.
    :return список чисел від 0 до limit включно"""
    my_range = range(limit + 1)  # включно
    return list(my_range)


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
    # create new list
    # iterate over function argument
    # cube current element
    # append it to new list
    # return new list
    return [element ** 3 for element in starting_list]


def crossword(amount_of_words: int, symbol_number: int) -> str:
    """На вхід програмі подається кількість слів та номер шуканого символу.
    Потім з консолі подається amount_of_words слів.
    :return слово, утворене з symbol_number-ого символу кожного слова"""
    words = []
    for letters_count in range(amount_of_words):
        word = input()
        words.append(word)
    final_string = ''
    for word in words:
        if symbol_number < len(word):
            final_string += word[symbol_number]
    return final_string


def list_from_string(string: str) -> list[str]:
    """На вхід програмі подається речення
    :return список з його слів"""
    return string.split()


def initials_2(path_components: list[str]) -> str:
    """На вхід програмі подається повний шлях до програми, де одна ланка - один елемент списку
    :return зʼєднаний шлях до програми (за сепаратор можна брати передній слеш /)"""
    return "/".join(path_components)


def ip_address_is_correct(ip_address: str) -> bool:
    """На вхід програмі подається ip-адреса.
    Вона є валідною, якщо кожен октет в межах від 0 до 255 влючно, а також є рівно 4 октети
    :return чи ip-адреса валідна

    127.0.0.1 - валідна
    194.624.5.1 - не валідна
    129.5.1.9.1 - не валідна"""
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True  # рішення супер


def separate_number_by_average_digit_value(number: int) -> str:
    """На вхід програмі подається ціле число.
    :return його, де між кожним символом буде -середнє значення двох сусідніх цифр-

    8714
    return: 8-7.5-7-4.0-1-2.5-4"""
    string_number = str(number)
    result = []
    for i in range(len(string_number)):
        first_number = int(string_number[i])
        second_number = int(string_number[i+1])
        average = (first_number + second_number) / 2
        result.extend([first_number, average])
    result.append(string_number[-1])
    return '-'.join(result)
