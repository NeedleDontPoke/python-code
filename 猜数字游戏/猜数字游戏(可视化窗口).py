"""created by guo_"""
import tkinter as tk, random


def main():
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def restart():
        random.randint(1, 10)
        main()

    def judge():
        if not is_number(ent.get()):
            tk.Label(win, text="不是数字", font=(None, 12), fg="orange").place(x=0, y=80)

        else:
            user_num = int(float(ent.get()))
            if user_num > 10 or user_num < 1:
                tk.Label(win, text="超出范围", font=(None, 12), fg="orange").place(x=0, y=80)
            elif user_num < r_num:
                tk.Label(win, text="你猜小了", font=(None, 12), fg="red").place(x=0, y=80)
            elif user_num > r_num:
                tk.Label(win, text="你猜大了", font=(None, 12), fg="red").place(x=0, y=80)
            elif user_num == r_num:
                tk.Label(win, text="你猜对了", font=(None, 12), fg="blue").place(x=0, y=80)
                btn.destroy()
                btn2 = tk.Button(win, text="再玩一次", font=(None, 12), command=lambda: [win.destroy(), restart()])
                btn2.place(x=90, y=30)

    r_num = random.randint(1, 10)

    win = tk.Tk()
    win.title("猜数字小游戏")
    win.iconbitmap("GUESSNUMICO.ico")
    win.geometry("300x120")
    win.resizable(False, False)

    tk.Label(win, text="请输入你猜的数字(1-10):", font=(None, 9)).place(x=0, y=3)
    ent = tk.Entry(win, font=(None, 10))
    ent.place(x=140, y=3)
    btn = tk.Button(win, text="OK", font=(None, 12), command=lambda: judge())
    btn.place(x=50, y=30)

    win.mainloop()


main()
