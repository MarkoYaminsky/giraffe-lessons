# Списки. Основні поняття (+ семантика) - len, sum, max, min, in, змінюваність списків,
# створення списків, методи списків для додавання елементів, видалення елементів, ітерація списків,
# join, split

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [1, 'string', True]  # not technically wrong, but looks like shit

# Ітератори: range, str, list
for element in my_list:
    print(element)

len(my_list)  # 9 - дожвина
sum(my_list)  # 45 - сума всіх елементів списку
max(my_list)  # 9 - найбільше число
min(my_list)  # 1 - найменше значення
5 in my_list  # True

# Mutability
my_list_3 = []
my_list_3 += [1, 2]
my_list_4 = my_list_3
my_list_3 is my_list_4  # True

# Copying
base_list = [1, 2, 4, 8, 9, 140]
inherited_list = base_list.copy()
inherited_list += [1513, 561]

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
