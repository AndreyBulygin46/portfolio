'''Условие задачи
Отсортируйте список курсов courses_list по длительности: от самого короткого к самому длинному. 
Выведите на экран сообщения вида «название курса — длительность курса».

Результат выведите в виде строк с текстом по примеру:

1
2
3
4
Python-разработчик с нуля - 12 месяцев
Java-разработчик с нуля - 14 месяцев
Fullstack-разработчик на Python - 20 месяцев
Frontend-разработчик с нуля - 20 месяцев
Помните, что могут встретиться курсы одинаковой длительности. Корректно обработайте эти случаи.

Самый простой способ сделать сортировку: создать новый словарь durations_dict с ключом duration 
и значением в виде исходного номера курса в courses_list.'''



# Наводим порядок: упорядочиваем курсы по продолжительности

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

# С этого момента начинается выполнение задания 2
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# Отсортируйте курсы по длительности (ключ duration), но при этом сохраните порядковый номер каждого курса из courses_list
# Самое простое — создать новый словарь durations_dict с ключом — duration и значением — исходным номером курса в courses_list
# Но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря — это список индексов, а не одно значение
durations_dict = {}

# Допишите код цикла так, чтобы в нём вы получали id курса. Подсказка: помните о функции enumerate
for id, dicts in enumerate(courses_list):

	key = dicts['duration'] # Получите значение из ключа duration
	# Допишите код ниже, который добавляет в словарь durations_dict по ключу key значения — id
	durations_dict[id] = key


# Отсортируем словарь по ключам. Этот код уже готов, ничего менять не нужно
# Здесь мы получаем пары ключ-значение в виде кортежа, и функция sorted выполняет сортировку по первым значениям кортежа — ключам
durations_dict = dict(sorted(durations_dict.items(), key=lambda i: i[1]))

# Выведите курсы, отсортированные по длительности
# Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения
for key,value in durations_dict.items():
	# Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность»

	print(f'{courses_list[key]['title']} - {value} месяцев')