def find_palindromes(starting_list: list[str]) -> list[str]:
    """Функція приймає список стрінгів.
    Ваше завдання: повернути список всіх букв всіх слів паліндромів

    Наприклад:
    list1 = ['модель', 'піп', 'качкодзьоб', 'радар']
    :return ['п', 'і', 'п', 'р', 'а', 'д', 'а', 'р']"""
    result = []  # дуже гарно # дякую, гав-гав
    [result.extend(word) for word in starting_list if (lowered_word := word.lower())[::-1] == lowered_word]
    return result


def even_odd_sort(starting_list: list[int]) -> list[int]:
    """
    Функція приймає список цілих чисел як вхідні дані
    та повертає новий список, який містить лише парні числа зі списку в порядку зростання,
    за якими слідують непарні числа зі списку у порядку зростання.
    """
    result = []
    for value in (0, 1):
        sample = [number for number in starting_list if number % 2 == value]
        sample.sort()
        result.extend(sample)
    return result


def replace_element(starting_list: list, element: int, replace_value: int) -> list[int]:
    """Функція приймає список чисел, шуканий елемент та значення-замінник.
    Ваше завдання: знайти останнє число зі значенням element та
    замінити його на нове значення replace_value
    :return список, у якому element замінений на replace_value"""
    if element not in starting_list:
        return starting_list

    copied_list = starting_list.copy()
    copied_list.reverse()

    index_to_replace = starting_list.index(element)
    starting_list[index_to_replace] = replace_value
    return starting_list


##########################################################################################


def filter_list(shopping_list: str):
    """Поданий список покупок, написаний через кому.
    :return розділену кожну покупку через абзац."""
    return "\n\n\t".join(shopping_list.split(","))


def lyrics(text: str):
    """Поданий текст пісні
    :return список з його слів та їх кількість"""

    def remove_punctuation(string: str):
        for symbol in (",", ".", "!", "?", "—", ":", ";"):
            string = string.replace(symbol, "")
        return string

    no_punctuation_text = remove_punctuation(text)
    return (final_list := no_punctuation_text.split()), len(final_list)


##########################################################################################


def no_ending(string: str):
    """На вхід програмі подається текст українською мовою
    :return слова з нульовим закінченням
    P.S. закінченням вважається голосна літера"""

    # consonants = "бвгґджзйлмнпрстфхцчшщь"
    # result = []
    # 
    # for word in string.split():
    #     last_consonant_position = len(word) - 1
    #     for symbol in word[::-1]:
    #         if symbol in consonants:
    #             break
    #         last_consonant_position -= 1
    #     if (lowered_word := word.lower())[
    #         : last_consonant_position + 1
    #     ] == lowered_word:
    #         result.append(word)
    # 
    # return result

    return [word for word in string.split() if word[-1] not in 'аеуоиіїєюя']


def more_than_four_vowels(string: str):
    """На вхід програмі подається стрічка
    :return слова, які мають більше ніж 4 голосні літери"""
    vowels = "аіуеоиюяєї"
    result = []

    for word in string.split():
        vowels_count = 0
        for symbol in word:
            if symbol in vowels:
                vowels_count += 1
        if vowels_count >= 4:
            result.append(word)

    return result
