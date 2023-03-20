def sum_of_numbers() -> int:
    """Людина вводить довільну кількість чисел з консолі. Прослуховувати ввід до тих пір, поки введене число
    не дорівнюватиме нулю
    :return суму всіх введених чисел"""
    number = int(input())
    sum_value = 0
    while number != 0:
        sum_value += number
        number = int(input())
    return sum_value


def input_code_word(code_word: str, attempt_limit: int) -> str:
    """Ви - розробник секретного сайту. До вас можуть зайти лише люди, які знають пароль від сайту.
    На вхід програмі подається кодове слово - пароль до сайту, а також кількість можливих невдалих спроб.
    Напишіть програму, в якій користувач буде вводити пароль з клавіатури, і якщо число спроб перевищує ліміт,
    то повертає фразу 'failure'. Якщо користувач вводить пароль правильно за відведені спроби, то повертає 'success'
    :return success або failure відповідно до завдання"""
    attempt_count = 0
    while attempt_count < attempt_limit:
        password = input()
        if password == code_word:
            return 'success'
        attempt_count += 1
    return 'failure'


def all_prime_numbers(limit: int) -> int:
    """На вхід програмі подається число.
    :return Кількість простих чисел від 2 до limit включно."""
    prime_numbers_count = 0
    for i in range(2, limit + 1):
        number_of_dividers = 0
        for j in range(2, i + 1):
            if i % j == 0:
                number_of_dividers += 1
        if number_of_dividers == 2:
            prime_numbers_count += 1
    return prime_numbers_count


def third_digit(number: int) -> int:
    """На вхід програмі подається число.
    :return Його третю цифру.
    * Подумайте про десяткові розряди, ділення на 10 в степені etc"""
    while number > 999:
        number //= 10
    return number % 10


def code_review() -> int:
    """Програма виконує таку функцію: на обробку поступає натуральне число. Вона повертає суму парних цифр цього числа.
    Якщо парних цифр нема, то виводить 0. Однак код написаний не правильно. Потрібно виправити цей код."""
    number = int(input("Введіть число: "))
    sum_value = 0
    while number != 0:
        if number % 2 == 0:  # +
            sum_value += number % 10
        number //= 10
    return sum_value
