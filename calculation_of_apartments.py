"""Расчет квартир и подездов"""
def calculation_of_apartments(flat: int,
                              total_number_of_apartments: int,
                              total_number_of_entrances: int,
                              total_number_of_floors: int):

    number_of_apartments = total_number_of_apartments / total_number_of_entrances   # узнаем количество квартир в подъезде
    apartments_per_floor = number_of_apartments / total_number_of_floors            # узнаем количество квартир на этаж
    entrance = flat // number_of_apartments \
               if flat % number_of_apartments == 0 \
               else (flat // number_of_apartments) + 1                      # узнаем подъезд, считается как кв/количество кв в подъезде, если флоат то +1

    floor_of_first_entrance = flat - (number_of_apartments * (entrance-1))  # кв по первому подъезду
    floor = floor_of_first_entrance // apartments_per_floor \
            if floor_of_first_entrance % apartments_per_floor == 0 \
               else (floor_of_first_entrance // apartments_per_floor) + 1

    return print(f'Квартира: {flat}, Этаж: {int(floor)}, Подъезд: {int(entrance)}')


flat = input('Введите номер квартиры: ') # кв
total_number_of_apartments = input('Введите количество квартир в доме: ') #кв в доме
total_number_of_entrances = input('Введите количество подъездов в доме: ') # колво подъездов в доме
total_number_of_floors = input('Введите количество этажей в доме: ') # колвл этажей
calculation_of_apartments(int(flat), int(total_number_of_apartments), int(total_number_of_entrances), int(total_number_of_floors))