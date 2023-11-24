import os
import requests
import sys
import tkinter as tk
import webbrowser

from bs4 import BeautifulSoup


def text_check(check_text):
    def none(text):
        tips_win = tk.Tk()
        tips_win.title(check_text)
        width = 230
        height = 35
        screenwidth = tips_win.winfo_screenwidth()
        screenheight = tips_win.winfo_screenheight()
        tips_win.geometry("%dx%d+%d+%d" % (
            width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
        tips_win.resizable(False, False)
        tk.Label(tips_win, text=text, font=(None, 20), fg="orange", justify="center").pack()
        tips_win.mainloop()

    def save_win():

        def txt_create(get):
            os.path.relpath(sys.argv[0])
            full_path = ent2.get() + '.txt'
            file = open(full_path, 'w', encoding="utf-8")
            file.write(get)
            win2.destroy()

        win2 = tk.Tk()
        win2.title('save')
        width = 300
        height = 80
        screenwidth = win2.winfo_screenwidth()
        screenheight = win2.winfo_screenheight()
        win2.geometry("%dx%d+%d+%d" % (
            width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
        win2.resizable(False, False)
        tk.Label(win2, text='project name:', font=(None, 13)).place(x=10, y=10)
        ent2 = tk.Entry(win2, font=(None, 11))
        ent2.place(x=130, y=12)
        ent2.get()
        tk.Button(win2, text='finish', font=(None, 15), command=lambda: txt_create(x.prettify())).place(x=60,
                                                                                                        y=40)
        tk.Button(win2, text='cancel', font=(None, 15), command=lambda: win2.destroy()).place(x=160, y=40)
        win2.mainloop()

    if check_text == "":
        none("输入框不能为空")
    else:
        try:
            url = check_text
            str_html = requests.get(url)
            txt = str_html.text
            x = BeautifulSoup(txt)
            html_win = tk.Tk()
            html_win.title("抓取")
            html_win.geometry("300x70")

            html_win.resizable(False, False)
            tk.Label(html_win, text=(web_ent.get(), "成功"), font=(None, 14), justify="center").pack()
            save = tk.Button(html_win, text="保存", width=10, activeforeground="gray", command=lambda: save_win())
            save.place(x=20, y=30)
            tk.Button(html_win, text="完成", activeforeground="black", command=lambda: html_win.destroy(),
                      width=10).place(x=110, y=30)
            open_web = tk.Button(html_win, text="用浏览器打开", activeforeground="gray",
                                 command=lambda: webbrowser.open(web_ent.get()))
            open_web.place(x=200, y=30)
            html_win.mainloop()
        finally:
            none("无效的地址")


root = tk.Tk()
root.title("Web Tools")
width = 398
height = 198
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (
    width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
root.resizable(False, False)

tips_text = "Web Tools 将根据你所输入的地址进行分析和打开。\n\n\n打开:"
tk.Label(root, text=tips_text, font=(None, 11), justify="left").pack()
web_ent = tk.Entry(root, font=(None, 10), width=45)
web_ent.place(x=65, y=48)
btn_check = tk.Button(root, text="分析", font=(None, 12), width=10, activeforeground="gray",
                      command=lambda: text_check(web_ent.get()))
btn_check.place(x=50, y=100)
tk.Button(root, text="取消", font=(None, 12), width=10, activeforeground="black",
          command=lambda: sys.exit()).place(x=258, y=100)

root.mainloop()
