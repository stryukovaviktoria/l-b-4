# Структура словника
# Автор:Стрюкова Вікторія, Перший студент
# Створено словник для зберігання інформації про успішність студентів групи
students = {
    'Group_101': [
        {
            'name': 'Стрюкова Вікторія',
            'course': 2,
            'subjects': {
                'Математика': [85, 90, 88],
                'Фізика': [75, 80, 72],
                'Інформатика': [90, 92, 95]
            }
        },
        {
            'name': 'Стрюкова Вікторія',
            'course': 2,
            'subjects': {
                'Математика': [70, 75, 78],
                'Фізика': [80, 82, 79],
                'Інформатика': [85, 87, 90]
            }
        }
    ]
}


# Автор:Стрюкова Вікторія, Перший студент
# Функція для додавання нового студента до групи
def add_student(students, group, name, course, subjects):
    if group not in students:
        students[group] = []

    students[group].append({
        'name': name,
        'course': course,
        'subjects': subjects
    })
    print(f"Студента {name} додано до групи {group}.")


# Використання функції додавання
new_student_subjects = {
    'Математика': [80, 85, 88],
    'Фізика': [78, 82, 80],
    'Інформатика': [88, 90, 93]
}
add_student(students, 'Group_101', 'Стрюкова Вікторія', 2, new_student_subjects)


# Автор:Стрюкова Вікторія, Другий студент
# Функція для сортування студентів за середньою оцінкою
def sort_students_by_average(students, group, subject=None):
    if group in students:
        if subject:
            # Сортування за середньою оцінкою з конкретного предмету
            sorted_students = sorted(students[group],
                                     key=lambda x: sum(x['subjects'][subject]) / len(x['subjects'][subject]),
                                     reverse=True)
        else:
            # Сортування за загальною середньою оцінкою
            sorted_students = sorted(students[group], key=lambda x: sum(
                [sum(grades) / len(grades) for grades in x['subjects'].values()]) / len(x['subjects']), reverse=True)

        # Виведення відсортованих студентів
        for student in sorted_students:
            print(f"Студент: {student['name']}, Курс: {student['course']}")
    else:
        print(f"Група {group} не знайдена.")


# Використання функції сортування
print("\nСортування студентів за загальною середньою оцінкою:")
sort_students_by_average(students, 'Group_101')

# Сортування за предметом "Математика"
print("\nСортування студентів за середньою оцінкою з математики:")
sort_students_by_average(students, 'Group_101', 'Математика')
