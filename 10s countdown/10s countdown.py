"""created by guo_"""
import _tkinter
import time
import tkinter as tk
import winsound


class Windows(tk.Tk):
    def __init__(self):
        super(Windows, self).__init__()
        self.f = None
        self.s = None
        self.num = 10
        self.width = 300
        self.height = 200
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.title("10s countdown")
        try:
            self.iconbitmap("timer.ico")
        except _tkinter.TclError:
            pass
        self.resizable(False, False)
        self.geometry("%dx%d+%d+%d" % (
            self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2))
        self.btn = tk.Button(self, text="start", state="active")
        self.btn.place(x=135, y=80)
        self.btn.config(command=self.text)
        self.lbl = tk.Label(self, font=(self, 12), text="10", fg="red", justify="center")
        self.lbl.place(x=143, y=30)

    def text(self):
        self.lbl.place_forget()
        self.lbl = tk.Label(self, font=(self, 12), text=self.num, fg="red", justify="center")
        self.lbl.place(x=143, y=30)
        self.btn.place_forget()
        self.btn = tk.Button(self, text="start", state="disabled")
        self.btn.place(x=135, y=80)
        self.s = self.lbl.after(1000, self.time)

    def time(self):
        self.num -= 1
        if self.num == -1:
            self.num = 10
            self.lbl.after_cancel(self.s)
            for i in range(2):
                for j in range(3):
                    winsound.Beep(1500, 130)
                time.sleep(0.5)
            self.btn.place_forget()
            self.btn = tk.Button(self, text="start", state="active")
            self.btn.place(x=135, y=80)
            self.btn.config(command=self.text)
        else:
            self.text()


if __name__ == '__main__':
    win = Windows()
    win.mainloop()
