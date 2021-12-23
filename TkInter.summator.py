def summator():
    try:
        a = float(entry_1.get())
        b = float(entry_2.get())
        label.config(text="Сумма числе будет равна {}".format(a + b))
    except ValueError:
        label.config(text="Введены не числа")

import tkinter as tk
abc = tk.Tk()
entry_1 = tk.Entry(abc)
entry_2 = tk.Entry(abc)
entry_1.pack()
entry_2.pack()
label = tk.Label(abc, text="Сумма чисел = ")
label.pack()
button = tk.Button(abc, text='сложить числа', command=summator)
button.pack()
abc.mainloop()
