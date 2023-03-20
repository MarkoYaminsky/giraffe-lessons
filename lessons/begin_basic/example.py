def validate_password(password: str) -> bool:
    """

    :return: Чи пароль валідний
    """
    ...
    ...
    ...
    password_is_valid = ...
    return password_is_valid


# data types
integer_variable = 1
float_variable = 2.5
string_variable = "string '123'"
string_variable_2 = 'string "123"'
bool_variable = True

# # console
# print(integer_variable, float_variable, string_variable, sep=', ')
# print(string_variable_2, bool_variable, end=' | ')
# print(integer_variable, bool_variable)
# # 1, 2.5, string '123'
# # string "123" | 1 True

# some_number = int(input("Введіть число: "))
# print(some_number + 5)
#
# some_word = input("Введіть стрічку: ")
# print(some_word * 10)

# Числа
a, b = int(input()), int(input())
sum_value = a + b
subtract_value = a - b
multiplication_value = a * b
division_value = a / b
modulo_division_value = a % b  # Остача при діленні
power_value = a ** b  # Степінь
whole_number_division_value = a // b  # Ділення без остачі

# Умовний оператор
if a > b:
    print('a is greater than b')
else:
    print('b is greater than a')

if a < 10:
    print('<10')
elif a < 17:
    print('<17')
elif a < 25:
    print('<25')
else:
    print('>25')

# <, <=, >, >=, ==

if 10 > a > 17 and a % 2 == 0:
    pass
if a < 17 or a % 2 == 1:
    pass
if a < 17 or a % 2 == 1 and a % 2 == 0:
    pass
