# Списки. Основні поняття (+ семантика) - len, sum, max, min, in, змінюваність списків,
# створення списків, методи списків для додавання елементів, видалення елементів, ітерація списків,
# join, split

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [1, 'string', True]  # not technically wrong, but looks like shit

# Ітератори: range, str, list
for element in my_list:
    ...

print(f"Довжина: {len(my_list)}")  # 9 - дожвина
print(f"Сума всіх: {sum(my_list)}")  # 45 - сума всіх елементів списку
print(f"Найбільший елемент: {max(my_list)}")  # 9 - найбільше число
print(f"Найменший елемент: {min(my_list)}")  # 1 - найменше число
print(f"Чи елемент існує: {5 in my_list}")  # True

# Mutability
my_list_3 = []
my_list_4 = my_list_3
my_list_3 += [1, 2]
print(my_list_3 is my_list_4)  # True

# Copying
base_list = [1, 2, 4, 8, 9, 140]
inherited_list = base_list.copy()
print('base', base_list)
inherited_list += [1513, 561]
print('base', base_list, 'inherited', inherited_list)

# Appending
my_list.append(10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Extend
my_list.extend([11, 12, 13, 14, 15, 16])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Deleting
del my_list[13]
del my_list[3:6:2]
del my_list

# Iteration
# Direct
for element in my_list_2:
    print(element)

# Indirect
for i in range(len(my_list_2)):
    print(my_list_2[i])

# Split
string = "daryna_is_stado"
words = string.split("_")  # ['daryna', 'is', 'stado']
words_2 = string.split('_', 1)  # ['daryna', 'is_stado']

# Join
string_2 = '*'.join(words)  # 'daryna*is*stado'
string_3 = '1234567890'.join(words_2)  # 'daryna1234567890is_stado'

# Iterator type casting
some_string = '1234567890'
my_range = range(10)
some_list = ['1', '2', '3']
converted_list = list(my_range)  # [0, 1, 2, 3, ..., 9]
converted_list_2 = list(some_string)  # ['1', '2', '3', '4', ..., '0']
