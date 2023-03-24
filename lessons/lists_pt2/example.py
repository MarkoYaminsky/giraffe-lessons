
# Методи списків
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# insert
my_list.insert(4, 10)
print(f"After insertion: {my_list=}")  # [1, 2, 3, 4, 10, 5, 6, 7, 8]

# index
print(f"Index: {my_list.index(7)}")  # 7

# remove
my_list.remove(5)
print(f"After removal: {my_list=}")  # [1, 2, 3, 4, 10, 6, 7, 8]

# pop
print(f"Popped element: {my_list.pop()}")  # 8
print(f"Popped element by index: {my_list.pop(3)}")  # 4
print(f"List after pop: {my_list=}")  # [1, 2, 3, 10, 6, 7]

# count
print(f"Counted 3: {my_list.count(3)}")  # 1

# reverse
my_list.reverse()
print(f"Reversed list: {my_list=}")  # [7, 6, 10, 3, 2, 1]

# copy
new_list = my_list.copy()
print(f"Copied list: {new_list=}")  # [7, 6, 10, 3, 2, 1]

# clear
my_list.clear()
print(f"Cleared list: {my_list=}")  # []

# sort
new_list.sort()
print(f"Sorted list: {new_list=}")  # [1, 2, 3, 6, 7, 10]

# Спискові вирази
range(10)  # 0, 1, 2, 3, ..., 9
list_2 = []
for element in range(10):
    if element % 3 == 0:
        list_2.append(element ** 2)
    else:
        list_2.append(element - 1)

# Списковий вираз без умов
list_3 = []
for element in range(10):
    list_3.append(element ** 2)

# [дія for змінна in ітератор]
comprehension_1 = [element ** 2 for element in range(10)]
print(comprehension_1)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Списковий вираз з одним розгалуженням
list_4 = []
for element in range(10):
    if element % 3 == 0:
        list_4.append(element ** 2)

# [дія for змінна in ітератор if умова]
comprehension_2 = [element ** 2 for element in range(10) if element % 3 == 0]
print(comprehension_2)  # [0, 9, 36, 81]

# Списковий вираз з тернарним оператором
list_2 = []
for element in range(10):
    if element % 3 == 0:
        list_2.append(element ** 2)
    else:
        list_2.append(element - 1)

# [дія if умова else інша_дія for змінна in ітератор]
comprehension_3 = [element ** 2 if element % 3 == 0 else 'Дарина' for element in range(10)]
print(comprehension_3)  # [0, 0, 1, 9, 3, 4, 36, 6, 7, 81]

# Заміна двох елементів місцями
a = 10
b = 5
a, b = b, a

my_list[1], my_list[2] = my_list[2], my_list[1]
