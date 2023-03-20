def input_code_word(code_word: str, attempt_limit: int) -> str:
    """Ви - розробник секретного сайту. До вас можуть зайти лише люди, які знають пароль від сайту.
    На вхід програмі подається кодове слово - пароль до сайту, а також кількість можливих невдалих спроб.
    Напишіть програму, в якій користувач буде вводити пароль з клавіатури, і якщо число спроб перевищує ліміт,
    то повертає фразу 'failure'. Якщо користувач вводить пароль правильно за відведені спроби, то повертає 'success'
    :return success або failure відповідно до завдання"""
    attempt = 0
    while attempt < attempt_limit:
        password = input('Еnter your password: ')
        if password == code_word:
            return 'success'
        attempt += 1
    return 'failure'


def sum_of_numbers() -> int:
    """Людина вводить довільну кількість чисел з консолі. Прослуховувати ввід до тих пір, поки введене число
    не дорівнюватиме нулю
    :return суму всіх введених чисел"""
    number = int(input())
    result = 0
    while number != 0:
        result += number
        number = int(input())
    return result


def all_prime_numbers(limit: int) -> int:
    """На вхід програмі подається число.
    :return Кількість простих чисел від 2 до limit включно."""
    prime_count = 0
    counter = 0
    for number in range(2, limit + 1):
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter == 2:
            prime_count += 1
    return prime_count


def third_digit(number: int) -> int:
    """На вхід програмі подається число.
    :return Його третю цифру.
    * Подумайте про десяткові розряди, ділення на 10 в степені etc"""
    while number > 999:
        number //= 10
    return number % 10


def code_review() -> int:
    """Програма виконує таку функцію: на обробку поступає натуральне число. Вона повертає суму парних цифр цього числа.
    Якщо парних цифр нема, то виводить 0. Однак код написаний не правильно. Потрібно виправити код."""
    '''number = input("Введіть число: ")
    sum_value = 0
    while number > 10:
        if number % 2 == 1:
            sum_value = number % 10
        number //= 10
    return sum_value'''
    number = int(input("Введіть число: "))  # +
    sum_value = 0  # +
    while number > 0:  # +
        if number % 2 == 0:  # +
            sum_value += number % 10  # +
        number //= 10  # +
    return sum_value  # +
