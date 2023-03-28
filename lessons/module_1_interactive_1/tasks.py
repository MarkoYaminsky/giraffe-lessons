def find_palindromes(starting_list: list[str]) -> list[str]:
    """Функція приймає список стрінгів.
    Ваше завдання: повернути список всіх букв всіх слів паліндромів

    Наприклад:
    list1 = ['модель', 'піп', 'качкодзьоб', 'радар']
    :return ['п', 'і', 'п', 'р', 'а', 'д', 'а', 'р']"""
    palindromes = [word for word in starting_list if word == word[::-1]]
    list_to_return = []
    for word in palindromes:
        list_to_return.extend(word)
    return list_to_return


def even_odd_sort(starting_list: list[int]) -> list[int]:
    """
    Функція приймає список цілих чисел як вхідні дані
    та повертає новий список, який містить лише парні числа зі списку в порядку зростання,
    за якими слідують непарні числа зі списку у порядку зростання.
    """
    even_numbers = [num for num in starting_list if num % 2 == 0]
    odd_numbers = [num for num in starting_list if num % 2 != 0]

    even_numbers.sort()
    odd_numbers.sort()
    return even_numbers + odd_numbers


def replace_element(starting_list: list, element: int, replace_value: int) -> list[int]:
    """Функція приймає список чисел, шуканий елемент та значення-замінник.
    Ваше завдання: знайти останнє число зі значенням element та
    замінити його на нове значення replace_value
    :return список, у якому element замінений на replace_value"""
    starting_list.reverse()
    i = starting_list.index(element)
    starting_list[i] = replace_value
    starting_list.reverse()
    return starting_list


##########################################################################################

def filter_list(shopping_list: str):
    """Поданий список покупок, написаний через кому.
    :return розділену кожну покупку через 2 нові рядки та таб."""
    return "\n\n\t".join(shopping_list.split(","))


def lyrics(text: str):
    """Поданий текст пісні
    :return список з його слів та їх кількість
    """
    words_list = text.split()
    return words_list, len(words_list)


##########################################################################################

def no_ending(string: str):
    """На вхід програмі подається текст
    :return слова з нульовим закінченням
    P.S. закінченням вважається голосна літера"""
    words = string.split()
    vovels = "аоеуияюєї"
    need_words = []
    for word in words:
        if word[-1] in vovels:
            need_words.append(word)
    return need_words


def more_than_four_vowels(string: str):
    """На вхід програмі подається стрічка
    :return слова, які мають більше ніж 4 голосні літери"""
    words = string.split()
    vovels = "аоеуияюєї"
    need_word = []
    for word in words:
        counter = 0
        for leter in word:
            if leter in vovels:
                counter += 1
        if counter >= 4:
            need_word.append(word)
    return need_word
