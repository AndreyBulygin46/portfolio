import turtle as t

t.ht()
t.pensize(5)

for r in range(40, 0, -10):
  for i in range(6):
    t.color(255, 165, r * 6)
    t.fillcolor(162, r * 6, 255)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.rt(60)



import turtle as t

t.ht()
t.pensize(2)

for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6) 
        t.fillcolor(162, r * 6, 255) 
        t.begin_fill()
        for _ in range(4):
            t.forward(r)
            t.rt(90)
        t.end_fill()
        t.rt(60)

t.done()

import turtle as t

t.ht()

t.pensize(2)

for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6) 
        t.fillcolor(162, r * 6, 255) 
        t.begin_fill()
        for _ in range(3):
            t.forward(r)
            t.rt(120)
        t.end_fill()
        t.rt(60)

t.done()