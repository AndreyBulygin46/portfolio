"""Приложение для вопспроизведения фоновых шумов"""

# какие есть файлы bird.mp3, rain_and_ocean.mp3, sea.mp3, sverchki.mp3, water.mp3
# white_noise.mp3, white_noise_2.mp3, zvuki_na_ulice_goroda.mp3, zvuk_ulice.mp3, brown_noise.mp3
# kak_na_ulice.mp3,koster.mp3,street.mp3

# добавление новых звуков
# 1) прописываем кнопку
# 2) размещаем кнопку
# 3) создаем функцию для воспроизведения по кнопке(копировать с предыдущих)
# 4) добавить в громкость(новая функция, новое размещение громкости)
# 5) добавить в стоп
# 6) добавить в каждую фун воспроизведения в отключение scl_ .set(1.0)
# 7) если готово то скомпилировать новый файл pyinstaller --onefile --noconsole my_music_app.py

from tkinter import *
import pygame



pygame.init()       # инит пайгейма
pygame.mixer.init() # инициализация микшера

win = Tk()
win.title('Моя музычка')
win.geometry(f'800x700+{win.winfo_screenwidth()//2-400}+{win.winfo_screenheight()//2-350}')
win.resizable(False,False)

def none():# тут хранится общаю громкость
# def volume(eve):
#     if eve.cget('text') == '+':
#         try:
#             btn_bird.sound.set_volume(btn_bird.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_rain_and_ocean.sound.set_volume(btn_rain_and_ocean.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_sea.sound.set_volume(btn_sea.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_zvuki_na_ulice_goroda.sound.set_volume(btn_zvuki_na_ulice_goroda.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_zvuk_ulice.sound.set_volume(btn_zvuk_ulice.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_sverchki.sound.set_volume(btn_sverchki.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_water.sound.set_volume(btn_water.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_white_noise_2.sound.set_volume(btn_white_noise_2.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_white_noise.sound.set_volume(btn_white_noise.sound.get_volume() + 0.1)
#         except AttributeError:
#             pass
#     elif eve.cget('text') == '-':
#         try:
#                btn_bird.sound.set_volume(btn_bird.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_rain_and_ocean.sound.set_volume(btn_rain_and_ocean.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_sea.sound.set_volume(btn_sea.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_zvuki_na_ulice_goroda.sound.set_volume(btn_zvuki_na_ulice_goroda.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_zvuk_ulice.sound.set_volume(btn_zvuk_ulice.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_sverchki.sound.set_volume(btn_sverchki.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_water.sound.set_volume(btn_water.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_white_noise_2.sound.set_volume(btn_white_noise_2.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
#         # _________________________________________________________________________________________
#         try:
#             btn_white_noise.sound.set_volume(btn_white_noise.sound.get_volume() - 0.1)
#         except AttributeError:
#             pass
    pass

def volume_bird(scl_bird):
    """Функция звука для bird"""
    try:
        btn_bird.sound.set_volume(float(scl_bird))
    except:
        pass

def volume_scl_rain_and_ocean(scl_rain_and_ocean):
    """Функция звука для rain_and_ocean"""
    try:
        btn_rain_and_ocean.sound.set_volume(float(scl_rain_and_ocean))
    except:
        pass

def volume_sea(scl_sea):
    """Функция звука для sea"""
    try:
        btn_sea.sound.set_volume(float(scl_sea))
    except:
        pass

def volume_sverchki(scl_sverchki):
    """Функция звука для sverchki"""
    try:
        btn_sverchki.sound.set_volume(float(scl_sverchki))
    except:
        pass

def volume_water(scl_water):
    """Функция звука для water"""
    try:
        btn_water.sound.set_volume(float(scl_water))
    except:
        pass

def volume_white_noise(scl_white_noise):
    """Функция звука для white_noise"""
    try:
        btn_white_noise.sound.set_volume(float(scl_white_noise))
    except:
        pass

def volume_white_noise_2(scl_white_noise_2):
    """Функция звука для white_noise_2"""
    try:
        btn_white_noise_2.sound.set_volume(float(scl_white_noise_2))
    except:
        pass

def volume_zvuki_na_ulice_goroda(scl_zvuki_na_ulice_goroda):
    """Функция звука для zvuki_na_ulice_goroda"""
    try:
        btn_zvuki_na_ulice_goroda.sound.set_volume(float(scl_zvuki_na_ulice_goroda))
    except:
        pass

def volume_zvuk_ulice(scl_zvuk_ulice):
    """Функция звука для zvuk_ulice"""
    try:
        btn_zvuk_ulice.sound.set_volume(float(scl_zvuk_ulice))
    except:
        pass

def volume_brown_noise(scl_brown_noise):
    try:
        btn_brown_noise.sound.set_volume(float(scl_brown_noise))
    except:
        pass

def volume_kak_na_ulice(scl_kak_na_ulice):
    try:
        btn_kak_na_ulice.sound.set_volume(float(scl_kak_na_ulice))
    except:
        pass

def volume_koster(scl_koster):
    try:
        btn_koster.sound.set_volume(float(scl_koster))
    except:
        pass

def volume_street(scl_street):
    try:
        btn_street.sound.set_volume(float(scl_street))
    except:
        pass

def click_stop(botton):
    '''Отработка кнопки стопа'''
    if botton.cget('text') == 'Стоп':
        btn_bird.config(bg='green')
        btn_rain_and_ocean.config(bg='green')
        btn_sea.config(bg='green')
        btn_sverchki.config(bg='green')
        btn_white_noise.config(bg='green')
        btn_white_noise_2.config(bg='green')
        btn_zvuk_ulice.config(bg='green')
        btn_zvuki_na_ulice_goroda.config(bg='green')
        btn_water.config(bg='green')
        btn_brown_noise.config(bg='green')
        btn_kak_na_ulice.config(bg='green')
        btn_koster.config(bg='green')
        btn_street.config(bg='green')
        scl_bird.set(1.0)
        scl_rain_and_ocean.set(1.0)
        scl_sea.set(1.0)
        scl_sverchki.set(1.0)
        scl_white_noise.set(1.0)
        scl_white_noise_2.set(1.0)
        scl_zvuk_ulice.set(1.0)
        scl_zvuki_na_ulice_goroda.set(1.0)
        scl_water.set(1.0)
        scl_brown_noise.set(1.0)
        scl_kak_na_ulice.set(1.0)
        scl_koster.set(1.0)
        scl_street.set(1.0)
        pygame.mixer.stop()
    if botton.cget('text') == 'Пауза' and botton.cget('bg') == 'green':
        botton.config(bg='red')
        pygame.mixer.pause()
    elif botton.cget('text') == 'Пауза' and botton.cget('bg') == 'red':
        botton.config(bg='green')
        pygame.mixer.unpause() 

'''Функции для кнопок'''
def sound_bird():
    '''Запуск файла bird'''
    if btn_bird.cget('bg') == 'green':
        btn_bird.config(bg='red')
        sound = pygame.mixer.Sound("bird.mp3")
        sound.play(loops=-1)
        btn_bird.sound = sound
    else:
        btn_bird.config(bg='green')
        if hasattr(btn_bird, 'sound'):
            btn_bird.sound.stop()
            scl_bird.set(1.0)

def sound_rain_and_ocean():
    '''Запуск файла rain_and_ocean'''
    if btn_rain_and_ocean.cget('bg') == 'green':
        btn_rain_and_ocean.config(bg='red')
        sound = pygame.mixer.Sound("rain_and_ocean.mp3")
        sound.play(loops=-1)
        btn_rain_and_ocean.sound = sound
    else:
        btn_rain_and_ocean.config(bg='green')
        if hasattr(btn_rain_and_ocean, 'sound'):
            btn_rain_and_ocean.sound.stop()
            scl_rain_and_ocean.set(1.0)

def sound_sea():
    '''Запуск файла sea'''
    if btn_sea.cget('bg') == 'green':
        btn_sea.config(bg='red')
        sound = pygame.mixer.Sound("sea.mp3")
        sound.play(loops=-1)
        btn_sea.sound = sound
    else:
        btn_sea.config(bg='green')
        if hasattr(btn_sea, 'sound'):
            btn_sea.sound.stop()
            scl_sea.set(1.0)

def sound_sverchki():
    '''Запуск файла sverchki'''
    if btn_sverchki.cget('bg') == 'green':
        btn_sverchki.config(bg='red')
        sound = pygame.mixer.Sound("sverchki.mp3")
        sound.play(loops=-1)
        btn_sverchki.sound = sound
    else:
        btn_sverchki.config(bg='green')
        if hasattr(btn_sverchki, 'sound'):
            btn_sverchki.sound.stop()
            scl_sverchki.set(1.0)

def sound_water():
    '''Запуск файла water'''
    if btn_water.cget('bg') == 'green':
        btn_water.config(bg='red')
        sound = pygame.mixer.Sound("water.mp3")
        sound.play(loops=-1)
        btn_water.sound = sound
    else:
        btn_water.config(bg='green')
        if hasattr(btn_water, 'sound'):
            btn_water.sound.stop()
            scl_water.set(1.0)

def sound_white_noise():
    '''Запуск файла white_noise'''
    if btn_white_noise.cget('bg') == 'green':
        btn_white_noise.config(bg='red')
        sound = pygame.mixer.Sound("white_noise.mp3")
        sound.play(loops=-1)
        btn_white_noise.sound = sound
    else:
        btn_white_noise.config(bg='green')
        if hasattr(btn_white_noise, 'sound'):
            btn_white_noise.sound.stop()
            scl_white_noise.set(1.0)

def sound_white_noise_2():
    '''Запуск файла white_noise_2'''
    if btn_white_noise_2.cget('bg') == 'green':
        btn_white_noise_2.config(bg='red')
        sound = pygame.mixer.Sound("white_noise_2.mp3")
        sound.play(loops=-1)
        btn_white_noise_2.sound = sound
    else:
        btn_white_noise_2.config(bg='green')
        if hasattr(btn_white_noise_2, 'sound'):
            btn_white_noise_2.sound.stop()
            scl_white_noise_2.set(1.0)

def sound_zvuki_na_ulice_goroda():
    '''Запуск файла zvuki_na_ulice_goroda'''
    if btn_zvuki_na_ulice_goroda.cget('bg') == 'green':
        btn_zvuki_na_ulice_goroda.config(bg='red')
        sound = pygame.mixer.Sound("zvuki_na_ulice_goroda.mp3")
        sound.play(loops=-1)
        btn_zvuki_na_ulice_goroda.sound = sound
    else:
        btn_zvuki_na_ulice_goroda.config(bg='green')
        if hasattr(btn_zvuki_na_ulice_goroda, 'sound'):
            btn_zvuki_na_ulice_goroda.sound.stop()
            scl_zvuki_na_ulice_goroda.set(1.0)

def sound_zvuk_ulice():
    '''Запуск файла zvuk_ulicy'''
    if btn_zvuk_ulice.cget('bg') == 'green':
        btn_zvuk_ulice.config(bg='red')
        sound = pygame.mixer.Sound("zvuk_ulice.mp3")
        sound.play(loops=-1)
        btn_zvuk_ulice.sound = sound
    else:
        btn_zvuk_ulice.config(bg='green')
        if hasattr(btn_zvuk_ulice, 'sound'):
            btn_zvuk_ulice.sound.stop()
            scl_zvuk_ulice.set(1.0)

def sound_brown_noise():
    """'''Запуск файла brown_noise'''"""
    if btn_brown_noise.cget('bg') == 'green':
        btn_brown_noise.config(bg='red')
        sound = pygame.mixer.Sound("brown_noise.mp3")
        sound.play(loops=-1)
        btn_brown_noise.sound = sound
    else:
        btn_brown_noise.config(bg='green')
        if hasattr(btn_brown_noise, 'sound'):
            btn_brown_noise.sound.stop()
            scl_brown_noise.set(1.0)

def sound_kak_na_ulice():
    if btn_kak_na_ulice.cget('bg') == 'green':
        btn_kak_na_ulice.config(bg='red')
        sound = pygame.mixer.Sound("kak_na_ulice.mp3")
        sound.play(loops=-1)
        btn_kak_na_ulice.sound = sound
    else:
        btn_kak_na_ulice.config(bg='green')
        if hasattr(btn_kak_na_ulice, 'sound'):
            btn_kak_na_ulice.sound.stop()
            scl_kak_na_ulice.set(1.0)

def sound_koster():
    if btn_koster.cget('bg') == 'green':
        btn_koster.config(bg='red')
        sound = pygame.mixer.Sound("koster.mp3")
        sound.play(loops=-1)
        btn_koster.sound = sound
    else:
        btn_koster.config(bg='green')
        if hasattr(btn_koster, 'sound'):
            btn_koster.sound.stop()
            scl_koster.set(1.0)

def sound_street():
    if btn_street.cget('bg') == 'green':
        btn_street.config(bg='red')
        sound = pygame.mixer.Sound("street.mp3")
        sound.play(loops=-1)
        btn_street.sound = sound
    else:
        btn_street.config(bg='green')
        if hasattr(btn_street, 'sound'):
            btn_street.sound.stop()
            scl_street.set(1.0)

'''Кнопки по количеству звуков(9шт)'''
btn_bird                  = Button(win,text='Птицы',        height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_bird)
btn_rain_and_ocean        = Button(win,text='Дождь и океан',height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_rain_and_ocean)
btn_sea                   = Button(win,text='Море',         height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_sea)
btn_sverchki              = Button(win,text='Сверчки',      height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_sverchki)
btn_water                 = Button(win,text='Вода',         height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_water)
btn_white_noise           = Button(win,text='Белый шум',    height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_white_noise)
btn_white_noise_2         = Button(win,text='Белый шум 2',  height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_white_noise_2)
btn_zvuki_na_ulice_goroda = Button(win,text='Улица',        height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_zvuki_na_ulice_goroda)
btn_zvuk_ulice            = Button(win,text='Улица 2',      height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_zvuk_ulice)
btn_brown_noise           = Button(win,text='Корич. шум',   height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_brown_noise)
btn_kak_na_ulice          = Button(win,text='На улице',     height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_kak_na_ulice)
btn_koster                = Button(win,text='Костер',       height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_koster)
btn_street                = Button(win,text='Улица 3',      height=5,width=15,bg='green',font=('Arial',8, 'bold'), command=sound_street)

'''Расположение кнопок на экране'''
btn_bird.place(x=35, y=25)
btn_rain_and_ocean.place(x=150,y=25)
btn_sea.place(x=265,y=25)
btn_sverchki.place(x=380,y=25)
btn_water.place(x=495,y=25)
btn_white_noise.place(x=35,y=145)
btn_white_noise_2.place(x=150,y=145)
btn_zvuki_na_ulice_goroda.place(x=265,y=145)
btn_zvuk_ulice.place(x=380,y=145)
btn_brown_noise.place(x=495,y=145)
btn_kak_na_ulice.place(x=610,y=25)
btn_koster.place(x=610,y=145)
btn_street.place(x=35,y=265)

"""Ползунки громкости, расположение их и настр громкости по умолчанию"""
scl_bird                  = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_bird)
scl_rain_and_ocean        = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_scl_rain_and_ocean)
scl_sea                   = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_sea)
scl_sverchki              = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_sverchki)
scl_water                 = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_water)
scl_white_noise           = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_white_noise)
scl_white_noise_2         = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_white_noise_2)
scl_zvuki_na_ulice_goroda = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_zvuki_na_ulice_goroda)
scl_zvuk_ulice            = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_zvuk_ulice)
scl_brown_noise           = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_brown_noise)
scl_kak_na_ulice          = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_kak_na_ulice)
scl_koster                = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_koster)
scl_street                = Scale(win,to=1.0,from_=0.0,length=112,orient='horizontal',resolution=0.1,showvalue=False,command=volume_street)

scl_bird.set(1.0)
scl_rain_and_ocean.set(1.0)
scl_sea.set(1.0)
scl_sverchki.set(1.0)
scl_water.set(1.0)
scl_white_noise.set(1.0)
scl_white_noise_2.set(1.0)
scl_zvuki_na_ulice_goroda.set(1.0)
scl_zvuk_ulice.set(1.0)
scl_brown_noise.set(1.0)
scl_kak_na_ulice.set(1.0)
scl_koster.set(1.0)
scl_street.set(1.0)

scl_bird.place(x=35,y=107)
scl_rain_and_ocean.place(x=150,y=107)
scl_sea.place(x=265,y=107)
scl_sverchki.place(x=380,y=107)
scl_water.place(x=495,y=107)
scl_white_noise.place(x=35,y=230)
scl_white_noise_2.place(x=150,y=230)
scl_zvuki_na_ulice_goroda.place(x=265,y=230)
scl_zvuk_ulice.place(x=380,y=230)
scl_brown_noise.place(x=495,y=230)
scl_kak_na_ulice.place(x=610,y=107)
scl_koster.place(x=610,y=230)
scl_street.place(x=35,y=347)

'''Кнопка стоп и пауза с расположением'''
btn_stop  = Button(win,text='Стоп', height=5,width=20,font=('Arial',12, 'bold'),           command=lambda: click_stop(btn_stop)) 
btn_pause = Button(win,text='Пауза',height=5,width=10,font=('Arial',12, 'bold'),bg='green',command=lambda: click_stop(btn_pause))
btn_stop.place(x=305,y=560)
btn_pause.place(x=30,y=560)
def none2(): # тут хранятся кнопки громкости общей и лейблы
# '''Кнопки громкости с размещением и лейблом'''
# lab = Label(win,text='Громкость',font=('Arial',10,'bold'))
# lab.place(x=65,y=465)
# btn_plus  = Button(win,text='+',  command=lambda:  volume(btn_plus), width=10)
# btn_minus = Button(win, text='-', command=lambda: volume(btn_minus), width=10)
# btn_plus.place(x=60,y=490)
# btn_minus.place(x=60,y=515)
    pass


# функция для отслеживания нажатий левой клпвиши мыши и вывод в консоль
# КАК БУДЕТ ПРОГА ГОТОВА УДАЛИТЬ
# def click_mouse(eve):
#     print(f'x: {eve.x} y: {eve.y}')
# win.bind('<Button-1>',click_mouse)


win.mainloop()
