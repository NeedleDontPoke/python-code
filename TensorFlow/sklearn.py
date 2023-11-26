import time
from tkinter import *
from tkinter import messagebox
from threading import Thread


def main():
    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            messagebox.showinfo('提示', '下载完成!')
            button1.config(state=NORMAL)

    class InstallTaskHandler(Thread):

        def run(self):
            time.sleep(8)
            messagebox.showinfo('提示', '安装完成!')
            button2.config(state=NORMAL)

    def download():
        button1.config(state=DISABLED)
        DownloadTaskHandler(daemon=True).start()

    def install():
        button2.config(state=DISABLED)
        InstallTaskHandler(daemon=True).start()

    def show_about():
        messagebox.showinfo('关于', '作者: NeedleDontPoke(v1.0)')

    top = Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = Frame(top)
    button1 = Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = Button(panel, text='安装', command=install)
    button2.pack(side='bottom')
    button3 = Button(panel, text='关于', command=show_about)
    button3.pack(side='right')
    panel.pack(side='bottom')

    mainloop()


if __name__ == '__main__':
    main()
