def find_palindromes(starting_list: list[str]) -> list[str]:
    """Функція приймає список стрінгів.
    Ваше завдання: повернути список всіх букв всіх слів паліндромів

    Наприклад:
    list1 = ['модель', 'піп', 'качкодзьоб', 'радар']
    :return ['п', 'і', 'п', 'р', 'а', 'д', 'а', 'р']"""
    result_list = []
    for word in starting_list:
        if word == word[::-1]:
        for leter in word:
            result_list.append(leter)
    return result_list




def even_odd_sort(starting_list: list[int]) -> list[int]:
    """
    Функція приймає список цілих чисел як вхідні дані
    та повертає новий список, який містить лише парні числа зі списку в порядку зростання,
    за якими слідують непарні числа зі списку у порядку зростання.
    """
    even_number = []
    odd_number = []
    for sumbol in starting_list:
        if int(sumbol) % 2 == 0:
            even_number.append(sumbol)
        else :
            odd_number.append(sumbol)
    new_list = even_number.sort() + odd_number.sort()
    return new_list


def replace_element(starting_list: list, element: int, replace_value: int) -> list[int]:
    """Функція приймає список чисел, шуканий елемент та значення-замінник.
    Ваше завдання: знайти останнє число зі значенням element та
    замінити його на нове значення replace_value
    :return список, у якому element замінений на replace_value"""
    index = starting_list.rfind(element)
    return starting_list.replase(starting_list[index], replace_value)



##########################################################################################

def filter_list(shopping_list: str):
    """Поданий список покупок, написаний через кому.
    :return розділену кожну покупку через абзац."""
    string = shopping_list.split()
    return "\n\n\t".join(string)


def lyrics(text: str):
    """Поданий текст пісні
    :return список з його слів та їх кількість"""
    # symbol_list = ["-", "?", "!", ",", ".", ";", ":"]
    # new_list = []
    # for text.split() in text:
    #     if tex not in symbol_list:
    #         new_list.append(word_in_text)
    # return new_list, len(new_list)


    def remove_punctuation(string: str):
        for symbol in (',', '.', '!', '?', '—', ':', ';'):
            string = string.replace(symbol, '')
        return string

    no_punctuation_text = remove_punctuation(text)
    return (final_list := no_punctuation_text.split()), len(final_list)


##########################################################################################

def no_ending(string: str):
    """На вхід програмі подається текст
    :return слова з нульовим закінченням
     P.S. закінченням вважається голосна літера"""
    vovel = "аоуеиіїєяю"
    words = string.split()
    new_list = []
    for word in words:
        if word[:-1] in vovel:
            new_list.append(word)
    return new_list



def more_than_four_vowerls(string: str):
    """На вхід програмі подається стрічка
    :return слова, які мають більше ніж 4 голосні літери"""
    word = string.split()
    counter = 0
    for leter in word:
        if leter in "аоуеиіїєяю"
