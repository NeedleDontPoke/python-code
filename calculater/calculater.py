import tkinter as tk


def create_btn(text, col, row, cs, rs, px=(1, 1), py=(1, 1)):  # 函数生成按钮
    t = text
    t = t.replace('×', '*')
    t = t.replace('÷', '/')
    t = t.replace('x²', '**2')
    t = t.replace('1/x', '**(-1)')
    a = tk.Button(root, text=text, width=4, command=lambda: (text_print(t)))
    a.grid(column=col, row=row, columnspan=cs, rowspan=rs, padx=px, pady=py, sticky="NEWS")
    return a


def grid_rowconfigure(*rows):  # 函数填充行
    for i in rows:
        root.grid_rowconfigure(i, weight=1)


def grid_columnconfigure(*cols):  # 函数填充列
    for i in cols:
        root.grid_columnconfigure(i, weight=1)


def bind_print(event):  # 函数键盘事件输入算式
    global textchange, equal_is
    if event.keysym != 'Return':
        if event.keysym == 'BackSpace':
            a = str(textchange)[0:-1]
            textchange = a
        elif event.keysym == 'Delete':
            textchange = ''
        else:
            textchange = str(textchange) + str(event.char)
        la.configure(text=textchange)
        show_is()
        equal_is = False
    else:
        text_equal()


def text_print(x):  # 函数按钮输入算式
    global textchange, equal_is
    if x != '=':
        if x == '←':
            a = str(textchange)[0:-1]
            textchange = a
        elif x == 'C':
            textchange = ''
        else:
            textchange = str(textchange) + str(x)
        la.configure(text=textchange)
        show_is()
        equal_is = False
    if x == '=':
        text_equal()


def text_equal():  # 函数计算结果并上到输入框
    global textchange, equal_is
    if lab['text'] != '错误':
        if not equal_is:
            textchange = lab['text']
            la.configure(text=textchange)
            lab.configure(text='')
            equal_is = True


def show_is():  # 显示框内容
    global textchange
    if textchange != '':
        try:
            text_show = eval(textchange)
        except (SyntaxError, TypeError, NameError):
            lab.configure(text='错误')
        else:
            lab.configure(text=text_show)
    else:
        lab.configure(text='')


root = tk.Tk()  # 创建窗体
root.geometry('250x350')
root.iconbitmap("calculaterICO.ico")
root.resizable(False, False)
root.title('计算器')
root.bind('<Key>', bind_print)

equal_is = False  # 一些变量
textchange = ''

la = tk.Label(root, text='', bg='white', fg='black', font=('宋体', 24), anchor='w', relief='flat')  # 生成输入框
la.grid(column=0, row=0, columnspan=5, rowspan=1, sticky='we')

lab = tk.Label(root, bg='white', fg='grey', height=1, font=('宋体', 22), anchor='w', relief='flat')  # 生成显示框
lab.grid(column=0, row=1, columnspan=5, rowspan=1, sticky='we')

btn = {'1': create_btn('1', 0, 5, 1, 1), '2': create_btn('2', 1, 5, 1, 1), '3': create_btn('3', 2, 5, 1, 1),
       '4': create_btn('4', 0, 4, 1, 1), '5': create_btn('5', 1, 4, 1, 1), '6': create_btn('6', 2, 4, 1, 1),
       '7': create_btn('7', 0, 3, 1, 1), '8': create_btn('8', 1, 3, 1, 1), '9': create_btn('9', 2, 3, 1, 1),
       '0': create_btn('0', 0, 6, 2, 1), '.': create_btn('.', 2, 6, 1, 1), '=': create_btn('=', 4, 5, 1, 2),
       '+': create_btn('+', 3, 6, 1, 1), '-': create_btn('-', 3, 5, 1, 1), '*': create_btn('×', 3, 4, 1, 1),
       '/': create_btn('÷', 4, 4, 1, 1), '←': create_btn('←', 1, 2, 1, 1), 'C': create_btn('C', 2, 2, 1, 1),
       '(': create_btn('(', 3, 2, 1, 1), ')': create_btn(')', 4, 2, 1, 1), '**2': create_btn('x²', 3, 3, 1, 1),
       '**(-1)': create_btn('1/x', 4, 3, 1, 1)}  # 生成按钮

grid_rowconfigure(2, 3, 4, 5, 6)
grid_columnconfigure(0, 1, 2, 3, 4)

root.mainloop()
