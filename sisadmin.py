'''Условие задачи
Сисадмину Василию нужно срочно починить компьютеры, в которых злые пользователи сломали диски с данными.

Сколько компьютеров сможет починить Василий, если в магазине не все позиции в наличии, 
а в организацию разрешается закупать только модели дисков из указанного списка производителей manufacturers?

Выведите названия всех подходящих моделей дисков и количество дисков, которые купит Василий.

1
2
3
4
5
6
7
8
9
10
models = [
    '480 ГБ 2.5" SATA накопитель Kingston A400', 
    '500 ГБ 2.5" SATA накопитель Samsung 870 EVO', 
    '480 ГБ 2.5" SATA накопитель ADATA SU650', 
    '240 ГБ 2.5" SATA накопитель ADATA SU650', 
    '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', 
    '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER', 
    '480 ГБ 2.5" SATA накопитель WD Green', 
    '500 ГБ 2.5" SATA накопитель WD Red SA500'
]
available = [1, 1, 1, 1, 0, 1, 1, 0] (1 - есть, 0 - нет):

manufacturers = ['Intel', 'Samsung', 'WD']
В этом задании корректность работы кода проверяется тестом. 
Для работы теста необходимо написать код функции. Обращайте внимание на подсказки к заданиям и комментарии в шаблоне кода.
Более подробно с синтаксисом функции вы сможете познакомиться на последующих занятиях.'''


def solve(models: list, available: list, manufacturers: list):
    repair_count = 0 # количество дисков, которые купит сисадмин
    ssds = [] # модели дисков из списка models, которые купит сисадмин
    in_stock = [] # новый пустой список, что есть в наличии
    # код вашего решения ниже:
    all_disk = zip(models,available) # объединили диски и наличие в zip

    for i,p in all_disk:             # итерируемся по объединенному списку zip
        if p == 1:
            in_stock.append(i)       # тут получился список тех дисков, которые есть в наличии
    for manufacturer in manufacturers:
        for stock in in_stock:
            if manufacturer in stock:
                ssds.append(stock)
                repair_count += 1


    return ssds, repair_count # Этот код менять не нужно

if __name__ == '__main__':
    # Этот код менять не нужно
    models = ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500']
    available = [1, 1, 1, 1, 0, 1, 1, 0]
    manufacturers = ['Intel', 'Samsung', 'WD']

    result = solve(models, available, manufacturers)
    assert result == (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2), \
        f"Неверный результат: {result}"
    print(f"Сисадмин Василий сможет купить диски: {result[0]} и починить {result[1]} компьютера")


