# guo_ create
import tkinter as tk, sys, os

i = 0
name = None


def hello(name):
    def nonewin(name):
        nonewin = tk.Tk()
        nonewin.title('print')
        nonewin.iconbitmap('ico/pen.ico')
        nonewin.geometry('200x20')
        nonewin.resizable(False, False)
        OKwin = tk.Label(nonewin, text='hello ' + name, font=(None, 12))
        OKwin.pack()
        nonewin.mainloop()

    if len(name) == 0:
        nonewin('None')

    else:
        nonewin(ent.get())


def ent2():
    def quit():
        win2.destroy()

    def txt_create():
        global name, i
        os.path.relpath(sys.argv[0])
        full_path = ent2.get() + '.txt'
        file = open(full_path, 'w')
        file.write('hello ' + ent.get())
        win2.destroy()

    global name, i
    win2 = tk.Tk()
    win2.title('save')
    win2.geometry("300x80")
    win2.iconbitmap('ico/save.ico')
    win2.resizable(0, 0)
    lbl_save = tk.Label(win2, text='project name:', font=(None, 13)).place(x=10, y=10)
    ent2 = tk.Entry(win2, font=(None, 11))
    ent2.place(x=130, y=12)
    name = ent2.get()
    btn3 = tk.Button(win2, text='finish', font=(None, 15), command=lambda: txt_create()).place(x=60, y=40)
    btn_c = tk.Button(win2, text='cancel', font=(None, 15), command=lambda: quit()).place(x=160, y=40)
    win2.mainloop()


def user_login_interrace_control_login():
    if user_name_ent.get() == 'guo_' and user_password_ent.get() == 'gzy20080520':
        login.quit()
    else:
        error = tk.Tk()
        error.resizable(0, 0)
        error.title('wrong')
        error.iconbitmap('ico/error.ico')
        error_lbl = tk.Label(error, text='error:your account or password is wrong or not filled in', font=(None, 12),
                             fg='red').pack()
        user_name_ent.delete(0, len(user_name_ent.get()));
        user_password_ent.delete(0, len(user_password_ent.get()))


login = tk.Tk()
login.title("ACCOUNT")
login.geometry('300x118')
login.iconbitmap('ico/login.ico')
login.resizable(0, 0)

user_name_lbl = tk.Label(login, text='  name:  ', font=(None, 12)).place(x=15, y=10)
user_name_ent = tk.Entry(login, font=(None, 12))
user_name_ent.place(x=100, y=10)

user_password_lbl = tk.Label(login, text='password:', font=(None, 12)).place(x=15, y=40)
user_password_ent = tk.Entry(login, font=(None, 12), show='*')
user_password_ent.place(x=100, y=40)

user_login_btn = tk.Button(login, text='log in', font=(None, 15),
                           command=lambda: user_login_interrace_control_login()).place(x=70, y=70)
user_exit_btn = tk.Button(login, text='exit', font=(None, 15), command=lambda: sys.exit()).place(x=170, y=70)

login.mainloop()

try:
    if user_name_ent.get() == 'guo_' and user_password_ent.get() == 'gzy20080520':
        login.destroy()
        win = tk.Tk()
        win.iconbitmap('ico/user.ico')
        win.title('main program')
        win.geometry('300x150')
        win.resizable(0, 0)

        ent_lbl = tk.Label(win, text='input:', font=(None, 12)).place(x=30, y=10)
        ent = tk.Entry(win, font=(None, 12))
        ent.place(x=90, y=10)

        btn = tk.Button(win, text='print', font=(None, 24), command=lambda: hello(ent.get()))
        btn.place(x=40, y=50)

        btn2 = tk.Button(win, text='close', font=(None, 24), command=lambda: sys.exit())
        btn2.place(x=160, y=50)

        menubar = tk.Menu(win)
        filemenu = tk.Menu(menubar, tearoff=False)
        filemenu.add_command(label="退出", command=lambda: sys.exit())
        filemenu.add_separator()
        filemenu.add_command(label="保存", command=lambda: ent2())
        menubar.add_cascade(label="选项", menu=filemenu)
        win.config(menu=menubar)

        win.mainloop()  # 执行GUI
except:
    Ellipsis

# get 返回Entry内的值
# lambda 匿名函数
