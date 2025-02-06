""" Подсчет возраста человека. """
from datetime import datetime
from dateutil.relativedelta import relativedelta


Date_of_Birth = input('Введите дату рождения в формате день,месяц,год: ')
Date_of_Birth = datetime.strptime(Date_of_Birth, "%d,%m,%Y")
date_now = datetime.now()
rel_dif = relativedelta(date_now, Date_of_Birth)

print(f'Количество лет: {rel_dif.years}, месяцев: {rel_dif.months}, дней: {rel_dif.days}.')
