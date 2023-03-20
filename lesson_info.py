student_list = ['Марічка', 'бабуся даруся', 'Діана', 'баба саша']

STUDENTS = map(lambda x: '_'.join(x.split()).lower(), student_list)

lesson_name = 'lists pt.1'

LESSON_NAME = '_'.join(lesson_name.replace('.', '').split()).lower()
