from tkinter import Tk, Label, Entry


class Initialization(Tk):
    def __init__(self):
        super(Initialization, self).__init__()
        self.ent_get = None
        self.width = 300
        self.height = 200
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.title("test")
        self.resizable(True, True)
        self.geometry("%dx%d+%d+%d" % (
            self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2))
        self.lbl = Label(self, text="input box:", font=(self, 12))
        self.lbl.place(x=10, y=5)
        self.ent = Entry(self)
        self.ent.place(x=100, y=8)
        self.ent.delete(0, "end")
        self.ent.insert(0, "text")
        self.lbl_refresh = Label(self, text="text", font=(self, 12), fg="blue")
        self.lbl_refresh.place(x=20, y=100)
        self.refresh()

    def refresh(self):
        self.lbl_refresh.place_forget()
        self.lbl_refresh = Label(self, text=self.ent_get, font=(self, 12), fg="blue")
        self.lbl_refresh.place(x=20, y=100)
        self.lbl_refresh.after(50, self.manage)

    def manage(self):
        self.ent_get = self.ent.get()
        self.refresh()


if __name__ == '__main__':
    init = Initialization()
    init.mainloop()
