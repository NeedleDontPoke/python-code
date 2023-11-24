"""Select the File"""
from tkinter import Tk, filedialog, StringVar, Label, Entry, Button, ttk, DISABLED, ACTIVE
from ttkbootstrap import Style
from random import sample


class SF(Tk):
    def __init__(self):
        super(SF, self).__init__()
        theme_list = ['cyborg', 'journal', 'darkly', 'flatly', 'minty',
                      'united', 'cosmo', 'lumen', 'yeti', 'superhero', 'sandstone']
        self.choice = sample(theme_list, 1)[0]
        self.get = ""
        self.p = int
        self.return_: str = ""
        self.path_data: str = ""
        self.__style = Style(theme=self.choice)
        self.width = 300
        self.height = 200
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.title("selectFile")
        self.resizable(False, False)
        self.geometry("%dx%d+%d+%d" % (
            self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2))
        self.path = StringVar()
        Label(self, text="目标路径:").grid(row=0, column=0)
        self.ent = Entry(self, textvariable=self.path, state=DISABLED)
        self.ent.grid(row=0, column=1)
        self.select_file_btn = Button(self, text="选择文件", command=lambda: self.select_path())
        self.select_file_btn.grid(row=0, column=2)
        self.cancel_btn = ttk.Button(self, text="取消", style="success.Outline.TButton", command=lambda: self.control(0))
        self.cancel_btn.place(x=60, y=50)
        self.confirm_btn = ttk.Button(self, text="载入", style="success.TButton",
                                      command=lambda: self.control(1), state=DISABLED)
        self.confirm_btn.place(x=200, y=50)
        self.protocol(name="WM_DELETE_WINDOW", func=lambda: quit())

    def select_path(self):
        self.path_data = filedialog.askopenfilename(filetypes=[("xlsx", ".xlsx"), ("xlsm", ".xlsm")])
        self.path_data = self.path_data.replace("/", "\\")
        self.path.set(self.path_data)
        self.get = self.ent.get()
        if self.get != '':
            self.confirm_btn.destroy()
            self.confirm_btn = ttk.Button(self, text="载入", style="success.TButton",
                                          command=lambda: self.control(1), state=ACTIVE)
            self.confirm_btn.place(x=200, y=50)
        else:
            self.confirm_btn.destroy()
            self.confirm_btn = ttk.Button(self, text="载入", style="success.TButton",
                                          command=lambda: self.control(1), state=DISABLED)
            self.confirm_btn.place(x=200, y=50)

    def control(self, p: int):
        self.p = p
        if p == 0:
            del self.path_data
            exit()
        self.destroy()


SF_var = SF()
SF_var.mainloop()
