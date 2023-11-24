"""User Interface Index(MP)"""
import os
import sys
import subprocess
from tkinter import (Tk, Menu, ttk, messagebox, Scrollbar,
                     HORIZONTAL, X, Y, RIGHT, BOTTOM)
from load import loading, column, path_s


def start_file(filename):
    try:
        os.startfile(filename)
    except FileNotFoundError:
        subprocess.Popen(['xdg-open', filename])


class UII(Tk):
    def __init__(self):
        super(UII, self).__init__()
        self.width = 650
        self.height = 550
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.title("index - %s" % (path_s[0]))
        self.resizable(False, False)
        self.geometry("%dx%d+%d+%d" % (
            self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2))
        self.scrollBar = Scrollbar(self)
        self.scrollBar_x = Scrollbar(self, orient=HORIZONTAL)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        self.scrollBar_x.pack(side=BOTTOM, fill=X)
        self.menubar = Menu(self)
        self.file_menu = Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label="选择文件", command=lambda: os.execl(sys.executable, sys.executable, *sys.argv))
        self.file_menu.add_command(label="打开目录", command=lambda: start_file(r'%s' % (path_s[0])))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=lambda: self.destroy())
        self.menubar.add_cascade(label="选项", menu=self.file_menu)
        self.config(menu=self.menubar)
        self.tree = ttk.Treeview(self, yscrollcommand=self.scrollBar.set, xscrollcommand=self.scrollBar_x.set)
        self.tree.pack(side="top", pady=20)
        self.tree["columns"] = ("姓名", "年龄", "状况", "信息")
        for r in L[0]:
            self.tree.column(r, width=100)
            self.tree.heading(r, text=r)
        L.remove(L[0])
        for i in range(len(L)):
            self.tree.insert("", i, text=str(i + 1),
                             values=("%s" % L[i][0], "%s" % L[i][1], "%s" % L[i][2], '%s' % L[i][3]))
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_close())
        self.scrollBar.config(command=self.tree.yview)
        self.scrollBar_x.config(command=self.tree.xview)

    def on_close(self):
        if messagebox.askokcancel("退出", "真的要退出吗?"):
            self.destroy()


L: list[list] = loading(column)
UI = UII()
UI.mainloop()
