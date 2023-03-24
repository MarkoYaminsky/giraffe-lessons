student_list = ['григорій', 'з кіндером', 'Іванка', 'без кіндера']

STUDENTS = map(lambda x: '_'.join(x.split()).lower(), student_list)

lesson_name = 'lists pt.2'

LESSON_NAME = '_'.join(lesson_name.replace('.', '').split()).lower()
