# 3 групи
string = input()

# ГРУПА 1: Робота з регістром
# Capitalize - міняє першу літеру стрічки на велику, а всі решта на малі
print(f"Capitalize: {string.capitalize()}")
# Swapcase - міняє регістр
print(f"Swapcase: {string.swapcase()}")
# Title - кожному слові заміняє першу букву на велику, а решта на малі
print(f"Title: {string.title()}")
# Lower - перетворює стрічку до нижього регістру
print(f"Lower: {string.lower()}")
# Upper - перетворює стрічку до верхнього регістру
print(f"Upper: {string.upper()}")

# ГРУПА 2: Робота з вмітом стрічки
# Count - рахує кількість зустрічей підстрічок у нашій стрічці
print(f"Count: {string.count('a')}")
# Startswith - визначає, чи слово починається на певну підстрічку
print(f"Startswith: {string.startswith('a')}")
# Endswith - визначає, чи слово закінчується на певну підстрічку
print(f"Endswith: {string.endswith('a')}")
# Find, rfind - шукає індекс першої появи підстрічки в стрічці (find - зліва, rfind - справа)
# В разі відсутності повертає -1
print(f"Find: {string.find('a')}")
# Index, rindex - шукає індекс першої появи підстрічки в стрічці (find - зліва, rfind - справа)
# В разі відсутності видає помилку
print(f"Index: {string.index('a')}")
# Strip, lstrip, rstrip - Очищує всі появи підстрічки справа від стрічки, зліва, або в обох напрямках
print(f"Strip: {string.strip('a')}")
# Replace - заміняє один символ на інший
print(f"Replace: {string.replace('a', 'b')}")

# ГРУПА 3: Класифікація стрічок
# Isalnum - визначає, чи всі симвлои є або цифрами, або алфавітними (тобто буквами)
print(f"Isalnum: {string.isalnum()}")
# Isalpha - визначає, чи всі символи є буквами
print(f"Isalpha: {string.isalpha()}")
# Isdigit - визначає, чи всі символи є цифрами
print(f"Isdigit: {string.isdigit()}")
# Isspace - визначає, чи всі символи є пробілами ( :\ )
print(f"Isspace: {string.isspace()}")
# Islower - визначає, чи всі символи є нижнього регістру
print(f"Islower: {string.islower()}")
# Isupper - визначає, чи всі символи є верхнього регістру
print(f"Isupper: {string.isupper()}")
# Istitle - визначає, чи слова задовольняють вимоги написання заголовків (наче якби на них використали .title())
print(f"Istitle: {string.istitle()}")
