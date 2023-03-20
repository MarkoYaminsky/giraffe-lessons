def input_code_word(code_word: str, attempt_limit: int) -> str:
    """Ви - розробник секретного сайту. До вас можуть зайти лише люди, які знають пароль від сайту.
    На вхід програмі подається кодове слово - пароль до сайту, а також кількість можливих невдалих спроб.
    Напишіть програму, в якій користувач буде вводити пароль з клавіатури, і якщо число спроб перевищує ліміт,
    то повертає фразу 'failure'. Якщо користувач вводить пароль правильно за відведені спроби, то повертає 'success'
    :return success або failure відповідно до завдання"""
    attempt = input()
    number_of_attempts = 0
    while number_of_attempts < attempt_limit:
        if attempt == code_word:
            return 'success'
        else:
            number_of_attempts += 1
            attempt = input()
    return 'failure'


def sum_of_numbers() -> int:
    """Людина вводить довільну кількість чисел з консолі. Прослуховувати ввід до тих пір, поки введене число
    не дорівнюватиме нулю
    :return суму всіх введених чисел"""
    while True:
        summa = 0
        number = int(input())
        if number == 0:
            break
        summa += number
    return summa


def all_prime_numbers(limit: int) -> int:
    """На вхід програмі подається число.
    :return Кількість простих чисел від 2 до limit включно."""
    count = 0
    for i in range(2, limit + 1):
        number_of_deviders = 0
        for j in range(1, limit + 1):
            if i % j != 0:
                number_of_deviders += 1
        if number_of_deviders == 2:
            count += 1
    return count


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
    number = int(input("Введіть число: "))  # +
    sum_value = 0  # +
    while number > 0:  # +
        if number % 2 == 0:  # +
            sum_value += number % 10  # +
        number //= 10  # +
    return sum_value  # +
