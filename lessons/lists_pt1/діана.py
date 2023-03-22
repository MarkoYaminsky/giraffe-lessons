def create_list_to_(limit: int) -> list[int]:
    """На вхід програмі подається число - межа.
    :return список чисел від 0 до limit включно"""
    my_list = []
    for element in range(limit):
        my_list.append(element)
    return my_list


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
        object_list[1: -1]


def cubes_list(starting_list: list[int]) -> list[int]:
    """На вхід програмі подається список цілих чисел
    :return список з кубів цих чисел"""
    new_list = []
    for element in starting_list:
        new_element = element ** 3
        new_list.append(new_element)
    return new_list


def crossword(amount_of_words: int, symbol_number: int) -> str:
    """На вхід програмі подається кількість слів та номер шуканого символу.
    Потім з консолі подається amount_of_words слів.
    :return слово, утворене з symbol_number-ого символу кожного слова"""
    desigion = []
    for number_of_word in range(amount_of_words):
        word = input()
        if len(word) >= symbol_number - 1:
            desigion.append(word[symbol_number - 1])
    return "".join(desigion)


def list_from_string(string: str) -> list[str]:
    """На вхід програмі подається речення
    :return список з його слів"""
    return string.split(" ")


def initials_2(path_components: list[str]) -> str:
    """На вхід програмі подається повний шлях до програми, де одна ланка - один елемент списку
    :return зʼєднаний шлях до програми (за сепаратор можна брати передній слеш /)

    ['C:', 'Users', 'Projects']"""
    return "/".join(path_components)


def ip_address_is_correct(ip_address: str) -> bool:
    """На вхід програмі подається ip-адреса.
    Вона є валідною, якщо кожен октет в межах від 0 до 255 влючно, а також є рівно 4 октети
    :return чи ip-адреса валідна"""
    counter = 1
    if len(ip_address) == 16:
        counter = 0
        for element in range(4):
            octet = ip_address[4 * element: 4 * element + 5]
            if int(octet) >= 255:
                    counter += 1
    return counter == 0


def separate_number_by_average_digit_value(number: int) -> str:
    """На вхід програмі подається ціле чиcло.
    :return його, де між кожним символом буде -середнє значення двох сусідніх цифр-

    8714
    return: 8-7.5-7-4.0-1-2.5-4"""
    string = [number % 10]
    last_element=numb
    number = number // 10
    while number > 0:
        element = number % 10
        added_element = (element + string[-1]) / 2
        number = number // 10
        string.append(str(added_element))
        string.append(str(element))
    print(string)
    return "-".join(string[::-1])
