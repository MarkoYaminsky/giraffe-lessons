def find_palindromes(starting_list: list[str]) -> list[str]:
    """Функція приймає список стрінгів.
    Ваше завдання: повернути список всіх букв всіх слів паліндромів

    Наприклад:
    list1 = ['модель', 'піп', 'качкодзьоб', 'радар']
    :return ['п', 'і', 'п', 'р', 'а', 'д', 'а', 'р']"""
    final_list = []
    for word in starting_list:
        if word == word[::-1]: # то не таке? чи слово є паліндромом
            for char in word:
                final_list.append(char)
    return final_list


def even_odd_sort(starting_list: list[int]) -> list[int]:
    """
    Функція приймає список цілих чисел як вхідні дані
    та повертає новий список, який містить лише парні числа зі списку в порядку зростання,
    за якими слідують непарні числа зі списку у порядку зростання.
    """
    even_numbers = []
    odd_numbers = []
    for number in starting_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    even_numbers.sort()
    odd_numbers.sort()
    return even_numbers + odd_numbers


def replace_element(starting_list: list, element: int, replace_value: int) -> list[int]:
    """Функція приймає список чисел, шуканий елемент та значення-замінник.
    Ваше завдання: знайти останнє число зі значенням element та
    замінити його на нове значення replace_value
    :return список, у якому element замінений на replace_value"""
    if element in starting_list:
        index = len(starting_list) - 1 - starting_list[::-1].index(element)
        starting_list[index] = replace_value
    return starting_list

"привіт андрій"
"а все"
"а ні, не все"
"не все."
"to be continued"

"ЗРАДЖУЙ ГВАЛТУЙ МЕНЕ" # мг, окей .... це не був наказ для тебе... (це просьба))
"ПОКИ Є СИЛИ" # добре, якщо будеш гарно поводит

##########################################################################################

def filter_list(shopping_list: str):
    """Поданий список покупок, написаний через кому.
    :return розділену кожну покупку через абзац."""
    return "\n\n\t".join(shopping_list.split(", "))

def lyrics(text: str):
    """Поданий текст пісні
    :return список з його слів та їх кількість"""
    words_list = text.split()
    return words_list, len(words_list)

##########################################################################################

def no_ending(string: str):
    """На вхід програмі подається текст
    :return слова з нульовим закінченням
     P.S. закінченням вважається голосна літера"""
    vowels = ["а", "е", "у", "о", "и", "я", "ю", "є", "ї", "і"]
    words = string.split()
    for word in words:
        if word[-1] != vowels:
            return word


def more_than_four_vowels(string: str):
    """На вхід програмі подається стрічка
    :return слова, які мають більше ніж 4 голосні літери"""
    vowels = ["а", "е", "у", "о", "и", "я", "ю", "є", "ї", "і"]
    words_list = []
    words = string.split()
    counter = 0
    for letter in words:
        if letter in vowels:
            counter += 1
    if counter > 4:
        words_list.append(words)
    return words_list
"поміняй місцями ворд ліст і вордс, бо в аргументі ти вказуєш що саме ти додаєш"
