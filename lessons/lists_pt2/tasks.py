from functools import cache


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
    del initial_list[0]
    initial_list *= 2  # initial_list.extend(initial_list)
    initial_list.insert(3, 25)
    return initial_list


def rearrange_min_and_max(initial_list: list[int]):
    """На вхід програмі подається список чисел.
    :return список, в якому переставлені максимальне і мінімальне число
    * згадайте (а, б = б, а)"""
    minimum_index, maximum_index = [initial_list.index(function(initial_list)) for function in (min, max)]
    initial_list[maximum_index], initial_list[minimum_index] = initial_list[minimum_index], initial_list[maximum_index]
    return initial_list


def amount_of_articles(text: str):
    """На вхід програмі подається текст.
    :return загальну кількість артиклів a, an, the в тексті. Артиклі можуть бути довільного регістру"""
    articles = ['article' for element in text.lower().split() if element in ['a', 'an', 'the']]
    return len(articles)


def clear_comments(text: str):
    """На вхід програмі подається текст. Рядки розділені символом нового рядка.
    В тексті в кінці деяких рядків залишені коментарі (коментарі починаються з символу #)
    :return текст з очищеними коментарями"""
    lines = text.split('\n')

    @cache
    def comment_begining(line: str):
        return line.find('#')

    return [line[:comment_begining(line)].strip() if comment_begining(line) != -1 else line for line in lines]


def sort_all_digits(text: str):
    """На вхід програмі подається текст, в якому є цифри.
    :return стрічку з посортованих цифр, зʼєднаних за комою з пробілом"""
    digits_list = [symbol for symbol in text if symbol.isdigit()]
    digits_list.sort()
    return ', '.join(digits_list)


def length_of_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому один елемент - довжина одного слова"""
    return [len(word) for word in text.split()]


def filter_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому тільки слова довжиною понад 5 символів"""
    return [word for word in text.split() if len(word) > 5]


def palindomes_in_range(lower_limit: int, upper_limit: int):
    """На вхід програмі подаються межі.
    :return список всіх числових паліндромів в цих межах"""
    numbers = [str(number) for number in range(lower_limit, upper_limit + 1)]
    return [number for number in numbers if number == number[::-1]]


def get_all_digits(text: str):
    """На вхід програмі подається текст.
    :return список цифр з тексту"""
    return [symbol for symbol in text if symbol.isdigit()]
