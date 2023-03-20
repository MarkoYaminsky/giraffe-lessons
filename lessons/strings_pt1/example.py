string = '1shukh34'
string_2 = "1jcni17"
string_3 = """1231
12312412

65gr
fd
v
dfv

"""

range(5)  # 0, 1, 2, 3, 4
'sasha'  # 's', 'a', 's', 'h', 'a'

# Mutable
[1, 2, 'a', 4]  # 0bx1758938a57
[1, 2, 4]  # 0bx1758938a57

# Immutable
'sasha'  # 1asfjh8id
'sashab'  # fhnvliotu2

second_symbol = string[1]
last_symbol = string[-1]

# Довжина стрічки
length_of_string = len(string)
# Пройти по стрічці, після кожного символу виводити його
for i in range(length_of_string):
    print(string[i])

for symbol in string:
    print(symbol)

a = 'Andriy'
b = 'Daryna'
c = a + ' ' + b
print(c)
c += a
print(c)

name = 'Sashko'
age = 18
status = 'Student of LPNU'
print('My name is ' + name + ', I am ' + str(age) + ' years old. I am a ' + status)
print(f'My name is {name}, I am {age} years old. I am a {status}')  # same output as before

# Оператор in
print('s' in name)  # True
print('0' in name)  # False
print('ash' in name)  # True
print('sh0' in name)  # False
print('sashko' in name)  # False

# Перетворення типів даних
string_number = '1234'
number = int(string_number)

number_2 = 7242
string_number_2 = str(number_2)

# Зрізи
range(0, 7, 2)  # 0, 2, 4, 6
my_string = ''
for i in range(0, 7, 2):
    my_string += string[i]

string[0:7:2]

# 1 аргумент - початок
# 2 аргумент - кінець
# 3 аргумент - крок

# Обернена стрічка
reversed_string = string[::-1]

# Копія стрічки
new_string = string[::]

# Опускання аргументів
# від початку
string[:x]

# до кінця
string[y:]

# середина стрічки
string[:len(string) // 2]
