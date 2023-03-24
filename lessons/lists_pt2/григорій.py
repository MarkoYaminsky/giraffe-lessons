def multitask(initial_list: list[int]):
    """На вхід програмі подається список.
    :return список, в якому
    - Замінений другий елемент на 17
    - додано 4, 5, 6 в кінець списку
    - видалений перший елемент списку
    - подвоєні елементи (типу два рази такий самий список, але в одному)
    - вставлене число 25 за індексом 3
    всі дії треба виконувати в такому порядку"""
    initial_list[1] = 17
    initial_list.extend([4, 5, 6])
    initial_list.pop(0)
    initial_list.extend(initial_list)
    initial_list.insert(3, 25)
    return initial_list


def rearrange_min_and_max(initial_list: list[int]):
    """На вхід програмі подається список чисел.
    :return список, в якому переставлені максимальне і мінімальне число
    * згадайте (а, б = б, а)"""
    return [
        max(initial_list)
        if x == min(initial_list)
        else min(initial_list)
        if x == max(initial_list)
        else x
        for x in initial_list
    ]


def amount_of_articles(text: str):
    """На вхід програмі подається текст.
    :return кількість артиклів a, an, the в тексті. Артиклі можуть бути довільного регістру
    """
    articles = ["a", "an", "the"]
    text_list = text.lower().split()
    count = ["article" for x in articles for y in text_list if x == y]
    return len(count)


def clear_comments(text: str):
    """На вхід програмі подається текст. Рядки розділені символом нового рядка.
    В тексті в кінці деяких рядків залишені коментарі (коментарі починаються з символу #)
    :return текст з очищеними коментарями"""
    list_to_return = []
    for string in text.split("\n"):
        list_to_return.append(string.split("#", 1)[0])
    return "\n".join(list_to_return)


def sort_all_digits(text: str):
    """На вхід програмі подається текст, в якому є цифри.
    :return стрічку з посортованих цифр, зʼєднаних за комою з пробілом"""
    list1 = [number for number in range(10) if str(number) in text]
    return ", ".join(map(str, list1))
    # import re
    # numbers_list = re.findall('[0-9]+', str)
    # return ', '.join(numbers_list.sort())


def length_of_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому один елемент - довжина одного слова"""
    return [len(string) for string in text.split()]


def filter_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому тільки слова довжиною понад 5 символів"""
    return [string for string in text.split() if len(string) > 5]


def palindomes_in_range(lower_limit: int, upper_limit: int):
    """На вхід програмі подаються межі.
    :return список всіх числових паліндромів в цих межах"""
    numbers = [str(number) for number in range(lower_limit, upper_limit)]
    return [
        int(number)
        for number in numbers
        if number in numbers and number[::-1] in numbers
    ]


def get_all_digits(text: str):
    """На вхід програмі подається текст.
    :return список цифр з тексту"""
    return [symbol for symbol in text if symbol.isdigit()]
