import os
import shutil

from lesson_info import LESSON_NAME, STUDENTS


def create_file_with_task(lesson_name: str):
    os.chdir('lessons')
    os.mkdir(lesson_name)
    os.chdir(lesson_name)
    with open('tasks.py', 'w'):
        pass
    with open('example.py', 'w'):
        pass


def copy_files_for_all_students(students: list[str], lesson_name: str):
    os.chdir(f'lessons/{lesson_name}')
    for student in students:
        if not os.path.exists(f'{student.lower()}.py'):
            shutil.copy('tasks.py', f'{student.lower()}.py')


if __name__ == '__main__':
    if not os.path.exists(f'lessons/{LESSON_NAME}'):
        create_file_with_task(LESSON_NAME)
    else:
        with open(f'lessons/{LESSON_NAME}/tasks.py') as tasks:
            if tasks.read():
                copy_files_for_all_students(STUDENTS, LESSON_NAME)
