# Приложение фин. планирования


salary = 100000  # Заработная плата
percent_mortgage = 30  # Ипотека в %
percent_life = 50  # На жизнь в %

# Напишите свой код здесь

salary_in_year = salary * 12                                # зп за год
mortgage = salary_in_year / 100  * percent_mortgage         # траты по ипотеки за год
percent_life_in_year = salary_in_year / 100 * percent_life  # траты на жизнь за год
result = salary_in_year - (mortgage + percent_life_in_year) # накопления

print("Ипотека:", mortgage)
print("Накопления:", result)
