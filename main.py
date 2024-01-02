"""№1"""

# Исходный список курсов courses_list
courses_list = [
    {"title": "Java-разработчик с нуля", "mentors": ["Филипп Воронов", "Анна Юшина", ], "duration": 14},
    {"title": "Fullstack-разработчик на Python", "mentors": ["Евгений Шмаргунов", "Олег Булыгин", ], "duration": 20},
    {"title": "Python-разработчик с нуля", "mentors": ["Евгений Шмаргунов", "Олег Булыгин", ], "duration": 12},
    {"title": "Frontend-разработчик с нуля", "mentors": ["Владимир Чебукин", "Эдгар Нуруллин", ], "duration": 20},
]

# Создаем словарь с ключом "длительность" и значением "номер курса"
durations_dict = {}
for idx, course in enumerate(courses_list):
    duration = course["duration"]
    if duration not in durations_dict:
        durations_dict[duration] = []
    durations_dict[duration].append(idx)

# Сортируем длительности курсов
sorted_durations = sorted(durations_dict.keys())

# Выводим отсортированные курсы


def get_sorted_courses():
    sorted_ = {}
    for num, duration in enumerate(sorted_durations, start=1):
        for course_idx in durations_dict[duration]:
            course = courses_list[course_idx]
            sorted_[course['title']] = f'{duration} месяцев'
    return sorted_


assert get_sorted_courses().get('Python-разработчик с нуля') == '12 месяцев'
assert get_sorted_courses().get('Java-разработчик с нуля') != '12 месяцев'


# Это вы мне? Подсчитываем тёзок на каждом курсе

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

# Пройдем по каждому курсу из списка courses_list
for course in courses_list:
    # Создадим множество для уникальных имён без фамилий
    unique_names = set()

    # Создадим словарь для подсчета количества преподавателей с одинаковыми именами
    name_count = {}

    # Пройдем по списку преподавателей на данном курсе
    for mentor in course["mentors"]:
        # Разделим имя и фамилию
        full_name = mentor.split()
        first_name = full_name[0]

        # Если такое имя уже встречалось на этом курсе, увеличим счетчик
        if first_name in name_count:
            name_count[first_name] += 1
            # Добавим имя в множество уникальных имён
            unique_names.add(first_name)
        else:
            # Иначе создадим новую запись в словаре
            name_count[first_name] = 1

    # Создадим список для хранения тёзок на этом курсе
    same_name_list = []

    # Пройдем по списку преподавателей на данном курсе ещё раз
    for mentor in course["mentors"]:
        full_name = mentor.split()
        first_name = full_name[0]

        # Если имя встречается более одного раза и ещё не добавлено в список тёзок
        if first_name in unique_names and first_name not in same_name_list:
            same_name_list.append(mentor)

    # Если есть тёзки на этом курсе, выведем информацию
    if same_name_list:
        # Отсортируем список тёзок по алфавиту
        same_name_list.sort()
        # Выведем информацию о тёзках на курсе
        print(f'На курсе {course["title"]} есть тёзки: {", ".join(same_name_list)}')
