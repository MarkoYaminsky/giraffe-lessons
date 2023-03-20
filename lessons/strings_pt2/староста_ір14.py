# 1. Capitalize, title, lower, upper
def is_titled(credentials: str) -> bool:
    """На вхід програмі подається стрічка, в якій є імʼя і прізвище людини
    :return Чи й імʼя, і прізвище написані з великої букви"""
    return credentials.istitle()


def good_tone(string: str) -> bool:
    """На вхід програмі подається стрічка.
    Стрічка вважається хорошим тоном, якщо в ній є слово "хороший" в будь-якому регістрі
    :return Чи стрічка вважаєаться хорошим тоном"""
    return "хороший" in string.lower()


def lowercase_symbols_count(string: str) -> int:
    """На вхід програмі подається стрічка.
    :return Скільки в ній символів з нижнім регістром
    * Пробіли, особливі символи, а також цифри - не є символами нижнього регістру"""
    counter = 0  # ASHDASDHKASHDKJAHDKJASHK 1741893;;; AHKHJJD - 0
    for element in string:
        if element == element.lower():
            counter += 1
    return counter


# 2. Count, startswith, endswith, find, rfind, index, rindex, strip, lstrip, rstrip, replace
def count_of_words(string: str) -> int:
    """На вхід програмі подається стрічка.
    :return Скільки вона має слів"""
    title_case_string = string.title()
    counter = 0
    for element in title_case_string:
        if element == element.upper():
            counter += 1
    return counter


def decipher_input(string_count: int) -> int:
    """На вхід програмі подається кількість стрічок n, а потім вводиться n стрічок з клавіатури.
    :return Кількість стрічок, які містять принаймні 3 пари символів '11'"""
    string_counter = 0
    for i in range(string_count):
        string = input()
        element_counter = string.count("11")
        if element_counter >= 3:
            string_counter += 1
    return string_counter


def dotcom_or_dotua(domain: str) -> bool:
    """На вхід програмі подається домен.
    Він нам підходить, якщо закінчується на .com або .ua
    :return Чи домен нам підходить"""
    return domain.endswith(".com") or domain.endswith(".ua")


def most_frequent_symbol(string: str) -> str:
    """На вхід програмі подається стрічка.
    :return Символ, який зустрічається в ній найчастіше"""
    letter = string[0]
    for i in range(len(string)):
        if string.count(string[i]) > string.count(letter):
            letter = string[i]
    return letter


def first_and_last_appearance(string: str, symbol: str) -> int | tuple[int, int]:
    """На вхід програмі подається стрічка і символ.
    Якщо в стрічці немає символу, то повернути -1
    Якщо він є один раз, то повернути індекс єдиного входження
    Якщо він є понад два рази, то повернути індекси першого і останнього входження через кому
    :return Згідно з умовою
    """
    if string.count(symbol) <= 1:
        return string
    return string.rfind(symbol), string.find()


# 3. Isalnum, isalpha, isdigit, islower, isupper, isspace
def determine_case(string: str) -> str:
    """На вхід програмі подається стічка
    Якщо всі символи стрічки є в нижньому регістрі, тоді повернути слово 'lower'
    Якщо в верхньому, повернути 'upper'
    Якщо ні так ні так, повернути 'none'
    Цифри, пробіли та спеціальні символи не входять до клаисфікації за регістром
    :return Згідно з умовою"""
    if string.islower():
        return "lower"
    if string.isupper():
        return "upper"
    return "none"
