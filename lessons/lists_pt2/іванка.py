def multitask(initial_list: list[int]):
    """На вхід програмі подається список.
    :return список, в якому
    - Замінений другий елемент на 17
    - додано 4, 5, 6 в кінець списку
    - видалений перший елемент списку
    - подвоєні елементи (типу два рази такий самий список, але в одному)
    - вставлене число 25 за індексом 3
    всі дії треба виконувати в такому порядку"""
    del initial_list[1]
    initial_list.insert(1, 17)
    initial_list += [4, 5, 6]
    del initial_list[0]
    new_list = []
    for element in initial_list:
        new_list.append(element)
        new_list.append(element)
    new_list.insert(3, 25)
    return new_list


def rearrange_min_and_max(initial_list: list[int]):
    """На вхід програмі подається список чисел.
    :return список, в якому переставлені максимальне і мінімальне число
    * згадайте (а, б = б, а)"""
    index_min = initial_list.index(min(initial_list))
    index_max = initial_list.index(max(initial_list))
    initial_list[index_min], initial_list[index_max] = initial_list[index_max], initial_list[index_min]
    return initial_list


def amount_of_articles(text: str):
    """На вхід програмі подається текст.
    :return кількість артиклів a, an, the в тексті. Артиклі можуть бути довільного регістру"""
    prep_list = ['article' for element in text.lower().split() if element in ['a', 'an', 'the']]
    return len(prep_list)


def clear_comments(text: str):
    """На вхід програмі подається текст. Рядки розділені символом нового рядка.
    В тексті в кінці деяких рядків залишені коментарі (коментарі починаються з символу #)
    :return текст з очищеними коментарями"""
    new_text = []
    index = text.find('#')
    new_text += text[0:index]
    for word in text[index:]:
        if word == '\n':
            index_1 = text.index(word)
        elif word == '#':
            index_2 = text.index(word)
            new_text += text[index_1:index_2]
    return new_text


def sort_all_digits(text: str):
    """На вхід програмі подається текст, в якому є цифри.
    :return стрічку з посортованих цифр, зʼєднаних за комою з пробілом"""
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list_of_number = []
    for element in text:
        if element in number:
            list_of_number.append(element)
    list_of_number.sort()
    return ", ".join(list_of_number)


def length_of_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому один елемент - довжина одного слова"""
    new_list = [len(word) for word in text.split()]
    return new_list


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
