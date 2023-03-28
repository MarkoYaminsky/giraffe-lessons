student_list = ['білий песик', 'Ґудзик', 'не твій пес']

STUDENTS = map(lambda x: '_'.join(x.split()).lower(), student_list)

lesson_name = 'interactive lesson 1'

LESSON_NAME = '_'.join(lesson_name.replace('.', '').split()).lower()
