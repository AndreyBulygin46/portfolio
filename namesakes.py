'''Условие задачи
В этом задании вы должны для каждого курса в отдельности подсчитать,
сколько на нём встречается преподавателей-тёзок —
людей с одинаковыми именами и разными фамилиями.

После того как все тёзки обнаружены, вы должны вывести
название курса и список преподавателей-тёзок (с именем и фамилией в алфавитном порядке),
которые обучают студентов в рамках этого курса.

Как назвать переменные, решайте сами (советуем выбирать максимально осмысленные имена).
Вы можете придумать свой алгоритм, отличный от предложенного.

Важно соблюдать следующий формат вывода:

1
2
3
4
На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, ...
На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Александр Иванов, ...
На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Ульянцев, ...
На курсе Frontend-разработчик с нуля есть тёзки: Александр Фитискин, Александр Шлейко, ...
Это задание поможет вам систематизировать знания по словарям,
множествам и спискам, а также потренироваться в создании сложных алгоритмов,
поэтому вы увидите только общую структуру-намёк, каким может быть алгоритм.'''


# Это вы мне? Подсчитываем тёзок на каждом курсе

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]
# ПРЕДСТАВЛЮ ЧТО КОДА ВЫШЕ НЕТ ДЛЯ ПРИКОЛА
courses_list = [] # тут уже собран список из словарей
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

list_with_course = [] # сами курсы
list_with_fullname = [] # полные имена разделенные по курсам
unique_names = [] # все уникальные имена разделенные по курсам
list_names = [] # список имен по курсам
list_namesakes = [] # список тезок
for i in courses_list:
    cours = i['title']
    name_mentors = i['mentors']
    list_with_course.append(cours)
    list_with_fullname.append(name_mentors)

for full_name in list_with_fullname:
    name_list = set()
    for name in full_name:
        name_list.add(name.split()[0])
    unique_names.append(sorted(list(name_list)))


for full_name in list_with_fullname:
    lis = []
    for name in full_name:
        lis.append(name.split()[0])
    list_names.append(lis)

for index_for_list, names_list in enumerate(list_names):
    lis = []
    for index_for_name, name in enumerate(names_list):
        if list_names[index_for_list].count(name) > 1:
            lis.append(list_with_fullname[index_for_list][index_for_name])
    list_namesakes.append(lis)

zip_course_and_namesakes = zip(list_with_course, list_namesakes)
for course, name in zip_course_and_namesakes:
    print(f'На курсе {course} есть тёзки: {', '.join(sorted(name))}')



