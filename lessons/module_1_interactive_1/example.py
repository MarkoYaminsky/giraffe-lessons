# Tuple (кортеж)
example_tuple = (1, 2, 3, 4, 5, 6)  # tuple(range(1, 7))

example_tuple.index(1)
example_tuple.count(2)
# ... будь-які спискові методи, які не міняють струкутуру

# Семантика
my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
my_tuple: tuple[int, str, bool] = (1, 'Дарина', True)

# Кортеж з одного елемента
singular_tuple = (1,)

# Приклад використання кортежів для пар (декількох) характеристик одного і того самого елемента
animals = list[tuple[str, str]] = [('Дарина', 'Ґуздик'), ('Андрій', 'self')]

# Довільний ітератор
# Розпакування
a = 5
b = 6
a, b = b, a + b  # (a, b) = (b, a + b)
query = 'request_name', 'content', 'metadata'
request_name, content, metadata = query

# Залишковість
*request_data_part, meta_data_part = query

# Запаковування
new_query = request_name[::-1], content * 2, metadata
