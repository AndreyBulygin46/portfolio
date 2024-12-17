from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests as rs

win = Tk()
win.title('Курсы криптовалют')
width = win.winfo_screenwidth() // 2 - 200
length = win.winfo_screenheight() // 2 - 150
win.geometry(f'400x300+{width}+{length}')
win.resizable(False, False)

coins = ['Bitcoin',
         'Ethereum',
         'Solana',
         'Dogecoin',
         'Bittensor',
         'Litecoin',
         'Celestia'
         ]


def req_price(btn):
    """Запрос курса криптовалюты"""
    data = comp.get()
    url = "https://api.coingecko.com/api/v3/simple/price?" \
        f"ids={data}" \
        "&vs_currencies=usd&precision=2"
    response = rs.get(url)
    if response.status_code == 200 and data:
        response = response.json()
        price = response[data.lower()]['usd']
        lb_info.config(fg='green')
        lb_info.config(text=f'Стоимость {data}: {price} USD')
    else:
        if response.status_code != 200:
            mb.showerror('ошибка', f'Ошибка: {response.status_code}')
        elif not data:
            mb.showerror('ошибка', 'Список пуст')


lb = Label(win, text='Выберите криптовалюту из списка ниже:',
           font=('Consolas', 14, 'bold'))
lb.pack(pady=20)

comp = ttk.Combobox(win, values=coins,
                    font=('Arial', 10), width=25, state="readonly")
comp.pack()

btn_sending = Button(win, text='Отправить запрос',
                     font=('Consolas', 14, 'bold'),
                     command=lambda: req_price(btn_sending))
btn_sending.pack(pady=20)

lb_info = Label(win, font=('Consolas', 14, 'bold'))
lb_info.pack()

win.bind('<Return>', req_price)

win.mainloop()
