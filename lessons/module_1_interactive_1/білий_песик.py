def find_palindromes(starting_list: list[str]) -> list[str]:
    """Функція приймає список стрінгів.
    Ваше завдання: повернути список всіх букв всіх слів паліндромів

    Наприклад:
    list1 = ['модель', 'піп', 'качкодзьоб', 'радар']
    :return ['п', 'і', 'п', 'р', 'а', 'д', 'а', 'р']"""


def even_odd_sort(starting_list: list[int]) -> list[int]:
    """
    Функція приймає список цілих чисел як вхідні дані
    та повертає новий список, який містить лише парні числа зі списку в порядку зростання,
    за якими слідують непарні числа зі списку у порядку зростання.
    """


def replace_element(starting_list: list, element: int, replace_value: int) -> list[int]:
    """Функція приймає список чисел, шуканий елемент та значення-замінник.
    Ваше завдання: знайти останнє число зі значенням element та
    замінити його на нове значення replace_value
    :return список, у якому element замінений на replace_value"""


##########################################################################################

def filter_list(shopping_list: str):
    """Поданий список покупок, написаний через кому.
    :return розділену кожну покупку через абзац."""
    product_list = shopping_list.split(', ')
    return '\n\n\t'.join(product_list)


def lyrics(text: str):
    """Поданий текст пісні
    :return список з його слів та їх кількість"""
    words = text.split()
    garbage = ['-', ',', '.', '?', '!']
    for word in words:
        [word.replace(symbol, '') for symbol in garbage if symbol in word]
    return words, len(words)


# не йди
# побудь зі мною
##########################################################################################


def no_ending(string: str):
    """На вхід програмі подається текст
    :return слова з нульовим закінченням
     P.S. закінченням вважається голосна літера"""
    vowels = 'аоеуияюєї'
    words = string.split()
    return [word for word in words if not (word[-1] in vowels)]


def more_than_four_vowels(string: str):
    """На вхід програмі подається стрічка
    :return слова, які мають більше ніж 4 голосні літери"""
    vowels = 'аоеуияюєїАОЕУИЯЮЄЇ'
    words = string.split()
    list_to_return = []
    for word in words:
        counter = 0
        for vowel in vowels:
            counter += word.count(vowel)
            if counter > 4:
                list_to_return.append(word)
                break
    return list_to_return
