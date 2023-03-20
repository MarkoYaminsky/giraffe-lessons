# 1. Capitalize, title, lower, upper
def is_titled(credentials: str) -> bool:
    """На вхід програмі подається стрічка, в якій є імʼя і прізвище людини
    :return Чи й імʼя, і прізвище написані з великої букви"""
    return credentials.istitle()


def good_tone(string: str) -> bool:
    """На вхід програмі подається стрічка.
    Стрічка вважається хорошим тоном, якщо в ній є слово "хороший" в будь-якому регістрі
    :return Чи стрічка вважаєаться хорошим тоном"""
    return 'хороший' in string.lower()


def lowercase_symbols_count(string: str) -> int:
    """На вхід програмі подається стрічка.
    :return Скільки в ній символів з нижнім регістром
    * Пробіли, особливі символи, а також цифри - не є символами нижнього регістру"""
    counter = 0
    for symbol in string:
        if symbol != symbol.isupper():
            counter += 1
    return counter  # why isn`t it possible? why, you stupid bastard??


# 2. Count, startswith, endswith, find, rfind, index, rindex, strip, lstrip, rstrip, replace
def count_of_words(string: str) -> int:
    """На вхід програмі подається стрічка.
    :return Скільки вона має слів"""
    space_count = string.count(' ')
    return space_count + 1


def decipher_input(string_count: int) -> int:
    """На вхід програмі подається кількість стрічок n, а потім вводиться n стрічок з клавіатури.
    :return Кількість стрічок, які містять принаймні 3 пари символів '11'"""
    counter = 0
    for i in range(string_count):
        string = input()
        if string.count('11') >= 3:
            counter += 1
    return counter


def dotcom_or_dotua(domain: str) -> bool:
    """На вхід програмі подається домен.
    Він нам підходить, якщо закінчується на .com або .ua
    :return Чи домен нам підходить"""
    return domain.endswith('.com') or domain.endswith('.ua')


def most_frequent_symbol(string: str) -> str:
    """На вхід програмі подається стрічка.
    :return Символ, який зустрічається в ній найчастіше"""
    counter = 0
    popular_symbol = ''  # без_фантазії.py
    for symbol in string:
        if string.count(symbol) > counter:
            counter = string.count(symbol)
            popular_symbol = symbol
    return popular_symbol


def first_and_last_appearance(string: str, symbol: str) -> int | tuple[int, int]:
    """На вхід програмі подається стрічка і символ.
    Якщо в стрічці немає символу, то повернути -1
    Якщо він є один раз, то повернути індекс єдиного входження
    Якщо він є понад два рази, то повернути індекси першого й останнього входження через кому
    :return Згідно з умовою
    """
    if string.count(symbol) <= 1:
        return string.find(symbol)
    return string.find(symbol), string.rfind(symbol)


# 3. Isalnum, isalpha, isdigit, islower, isupper, isspace
def determine_case(string: str) -> str:
    """На вхід програмі подається стрічка
    Якщо всі символи стрічки є в нижньому регістрі, тоді повернути слово 'lower'
    Якщо в верхньому, повернути 'upper'
    Якщо ні так ні так, повернути 'none'
    Цифри, пробіли та спеціальні символи не входять до клаисфікації за регістром
    :return Згідно з умовою"""
    if string.islower():
        return 'lower'
    elif string.isupper():
        return 'upper'
    return 'none'
