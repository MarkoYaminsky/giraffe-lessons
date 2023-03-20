if __name__ == '__main__':
    # Списки. Основні поняття (+ семантика) - len, sum, max, min, in, незмінюваність списків,
    # створення списків, методи списків для додавання елементів, видалення елементів, ітерація списків,
    # join, split
    def create_list_to_(limit: int) -> list[int]:
        """На вхід програмі подається число - межа.
        :return список чисел від 0 до limit включно"""


    def get_list_info(object_list: list[int]) -> tuple:
        """На вхід програмі подається список чисел
        :return
        - довжина списка
        - останній елемент списка
        - список у зворотному порядку
        - чи список містить числа 5 та 17
        - той самий список, з видаленим першим та останнім елементом"""


    def cubes_list(starting_list: list[int]) -> list[int]:
        """На вхід програмі подається список цілих чисел
        :return список з кубів цих чисел"""


    def crossword(amount_of_words: int, symbol_number: int) -> str:
        """На вхід програмі подається кількість слів та номер шуканого символу.
        Потім з консолі подається amount_of_words слів.
        :return слово, утворене з symbol_number-ого символу кожного слова"""


    def list_from_string(string: str) -> list[str]:
        """На вхід програмі подається речення
        :return список з його слів"""


    def initials_2(path_components: list[str]) -> str:
        """На вхід програмі подається повний шлях до програми, де одна ланка - один елемент списку
        :return зʼєднаний шлях до програми (за сепаратор можна брати передній слеш /)"""


    def ip_address_is_correct(ip_address: str) -> bool:
        """На вхід програмі подається ip-адреса.
        Вона є валідною, якщо кожен октет в межах від 0 до 255 влючно, а також є рівно 4 октети
        :return чи ip-адреса валідна"""


    def separate_number_by_average_digit_value(number: int) -> str:
        """На вхід програмі подається ціле чило.
        :return його, де між кожним символом буде -середнє значення цифр числа-"""
    ...