"""Проект Холодильник"""
import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)}
    ],
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}]
}

def add(items, title, amount, expiration_date=None):
    """Добавляем товар в холодильник"""
    if expiration_date is not None:  # Если срок годности есть то преобразуем в формат datetime
        exp_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    else:  # Если отсутствует то None
        exp_date = None
    if items.get(title) is None :  # Продукта нет в холодильнике, добавляем
        items[title] = [{'amount': Decimal(amount), 'expiration_date': exp_date}]
    else:  # Продукт есть добавляем партию
        items[title].append({'amount': Decimal(amount), 'expiration_date': exp_date})


def is_date(date_str):
    """Проверяем строку на соответствие формату даты"""
    date_list = date_str.split('-')
    is_true = (len(date_list)==3
               and len(date_list[0])==4
               and len(date_list[1])==2
               and len(date_list[2])==2)
    return is_true

def add_by_note(items, note):
    """Добавляем товар из строки"""
    words = note.split()
    if not is_date(words[-1]):  # Если в строке отсутствует срок годности
        expiration_date = None
        amount = Decimal(words[-1])
        title = ' '.join(words[:len(words) - 1])
    else:  # Если срок годности присутствует
        expiration_date = words[-1]
        amount = Decimal(words[-2])
        title = ' '.join(words[:-2])
    add(items, title, amount, expiration_date)

def find(items, needle):
    """Поиск товара в холодильнике"""
    return [item for item in items if needle.lower() in item.lower()]


def amount(items, needle):
    """Выводим количество товара"""
    count = Decimal('0')
    index = 0
    item_list = find(items, needle)
    for _ in item_list:
        values = items.get(item_list[index])
        index +=1
        for value in values:
            count += Decimal(value['amount'])
    return count

def expire(items, in_advance_days=0):
    """Ищем просроченный товар"""
    current_data = datetime.date.today() + datetime.timedelta(days = in_advance_days)
    keys_list = list(items)
    expired_data_product = []
    for key in keys_list:
        count = Decimal(0)
        values = items.get(key)
        for value in values:
            if (value['expiration_date'] is not None
                and current_data >= value['expiration_date']):
                count += Decimal(value['amount'])
        if count !=0:
            expired_data_product.append((key,count))
    return expired_data_product
