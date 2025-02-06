'''1)

Нарисуйте три разных круга, используя разные цвета и радиусы, используя модуль turtle.
Для каждого круга используйте begin_fill(), color(), circle() и end_fill().

Сохраните файл с проектом на компьютер.'''

# импорт черепашки
import turtle as t

circle_1 = ['yellow','red', 15, 50] # цвет_пера, цвет заливки, радиус
circle_2 = ['green','blue', 20, 60]
circle_3 = ['red','green', 25, 0]

t.up()           # подняли перо
t.goto(-180,140) # переставили перо по координатам
t.down()         # опустили перо
# t.left(90)

# цикл фор по трем списками
for feather, fill, radius, indentation  in circle_1, circle_2, circle_3:
    t.color(feather)          # цвет пера
    t.fillcolor(fill)         # цвет заливки
    t.pensize(5)              # тощина пера
    t.begin_fill()            # начало заливки
    t.circle(radius)          # круг
    t.end_fill()              # конец заливки end_fill()
    t.up()                     # поднять перо up()
    t.forward(indentation)     # отступ
    t.down()                   # опустить перо down()

'''2)

Используя методы модуля turtle, нарисуйте несколько геометрических фигур:
прямоугольник, ромб и трапецию.
Каждая фигура должна быть закрашена в свой цвет, который сочетается с остальными.
Используйте цветовой круг Adobe для выбора красивого сочетания цветов.'''


t.up()
t.forward(100)
t.down()

# прямоугольник
t.color('red')
t.begin_fill()
length_1 = 40
length_2 = 20

for _ in range(2):
    t.forward(length_1)
    t.left(90)
    t.forward(length_2)
    t.left(90)
t.end_fill()


t.up()
t.goto(120,115)
t.down()
t.left(50)

# ромб
t.color('blue')
t.begin_fill()

t.forward(50)
t.left(80)
t.forward(50)
t.left(100)
t.forward(50)
t.left(80)
t.forward(50)

t.end_fill()

t.up()
t.goto(30, 50)
t.down()
t.left(50)

# трапеция
t.color('pink')
t.begin_fill()

t.forward(100) # нижняя линия
t.left(120)    # поворот от низа
t.forward(50)  # правая грань
t.left(60)     # поворт к верхней грани
t.forward(50)  # верхняя грань
t.left(60)     # поворот к нижней грани
t.forward(50)  # левая грань

t.end_fill()

'''3)

Нарисуйте зеленую елку из трех закрашенных треугольников.'''

t.color('green')
t.left(120)
t.up()
t.goto(-150,-150)
t.down()

t.begin_fill()
for _ in range(3):
    for _ in range(3):
        t.forward(40)
        t.left(120)
    t.left(90)
    t.up()
    t.forward(40)
    t.right(90)
    t.down()
t.end_fill()

'''4)

Нарисуйте три квадрата размером 30 на 30 на расстоянии 30 пикселей друг от друга.
Квадраты не должны соединятся зеленой линией.'''

t.up()
t.forward(100)
t.down()

for _ in range(3): 
    for _ in range(4):
        t.forward(30)
        t.left(90)
    t.up()
    t.forward(60)
    t.down()

t.done()