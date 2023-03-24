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
    initial_list *= 2
    initial_list.insert(3, 25)
    return initial_list


def rearrange_min_and_max(initial_list: list[int]):
    """На вхід програмі подається список чисел.
    :return список, в якому переставлені максимальне і мінімальне число
    * згадайте (а, б = б, а)"""
    min_el = min(initial_list)
    max_el = max(initial_list)
    min_index = initial_list.index(min_el)
    max_index = initial_list.index(max_el)
    initial_list[min_index], initial_list[max_index] = initial_list[max_index], initial_list[min_index]
    return initial_list


def amount_of_articles(text: str):
    """На вхід програмі подається текст.
    :return кількість артиклів a, an, the в тексті. Артиклі можуть бути довільного регістру"""
    words = text.split()
    count = 0
    for word in words:
        if word.lower() == ['a', 'an', 'the']:
            count += 1
    return count


def clear_comments(text: str):
    """На вхід програмі подається текст. Рядки розділені символом нового рядка.
    В тексті в кінці деяких рядків залишені коментарі (коментарі починаються з символу #)
    :return текст з очищеними коментарями"""
    lines = text.split('\n')
    result = []
    for line in lines:
        comment = line.find('#')
        if comment != -1:
            line = line[:comment]
        result.append(line)
    return result


def sort_all_digits(text: str):
    """На вхід програмі подається текст, в якому є цифри.
    :return стрічку з посортованих цифр, зʼєднаних за комою з пробілом"""
    digits = [symbol for symbol in text if symbol.isdigit()]
    digits.sort()
    return ', '.join(digits)


def length_of_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому один елемент - довжина одного слова"""
    words = text.split()
    length = [len(word) for word in words]
    return length


def filter_words(text: str):
    """На вхід програмі подається текст.
    :return список, в якому тільки слова довжиною понад 5 символів"""
    words = text.split()
    list_of_words = [word for word in words if len(word) > 5]
    return list_of_words


def palindomes_in_range(lower_limit: int, upper_limit: int):
    """На вхід програмі подаються межі.
    :return список всіх числових паліндромів в цих межах"""
    list_of_palindromes = [number for number in range(lower_limit, upper_limit + 1) if str(number) == str(number)[::-1]]
    return list_of_palindromes


def get_all_digits(text: str):
    """На вхід програмі подається текст.
    :return список цифр з тексту"""
    digits = [symbol for symbol in text if symbol.isdigit()]
    return digits
