from os import getcwd, system
from abc import ABCMeta, abstractmethod
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class Windows(Tk, metaclass=ABCMeta):
    __slots__ = ('_width', '_height')

    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self._height = height
        self.title('用户收货地址')
        self._screenwidth = self.winfo_screenwidth()
        self._screenheight = self.winfo_screenheight()
        self.geometry("%dx%d+%d+%d" % (self._width, self._height,
                                       (self._screenwidth - self._width) / 2, (self._screenheight - self._height) / 2))
        self.resizable(False, False)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def setting(self):
        pass


class DrawWindows(Windows):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.entry_vars = [StringVar() for _ in range(6)]
        self.menubar = Menu(self)
        self.file_menu = Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label='打开目录', command=self.open_current_directory)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='保存当前数据', command=lambda: self.save_text())
        self.file_menu.add_command(label='加载保存的数据', command=lambda: self.load_text())
        self.menubar.add_cascade(label='选项', menu=self.file_menu)
        self.config(menu=self.menubar)
        Label(self, font=('宋体', 12), text='地址:').place(x=20, y=30)
        Label(self, font=('宋体', 12), text='省').place(x=240, y=30)
        Label(self, font=('宋体', 12), text='市').place(x=440, y=30)
        Label(self, font=('宋体', 12), text='收件人:').place(x=10, y=120)
        Label(self, font=('宋体', 12), text='联系电话:').place(x=2, y=180)
        self.active = StringVar()
        self.combo = Combobox(self, font=('宋体', 14), width=2, textvariable=self.active)
        self.combo['value'] = ('区', '县')
        self.combo['state'] = 'readonly'
        self.province_entry = Entry(self, font=('楷体', 15), textvariable=self.entry_vars[0])
        self.city_entry = Entry(self, font=('楷体', 15), textvariable=self.entry_vars[1])
        self.district_entry = Entry(self, font=('楷体', 15), textvariable=self.entry_vars[2])
        self.address_entry = Entry(self, font=('楷体', 15), textvariable=self.entry_vars[3])
        self.recipient_entry = Entry(self, font=('楷体', 15), textvariable=self.entry_vars[4])
        self.contactnumber_entry = Entry(self, font=('楷体', 15), textvariable=self.entry_vars[5])
        self.save_button = Button(self, font=('宋体', 12), text='保存', command=self.save)
        self.clear_button = Button(self, font=('宋体', 12), text='清除', command=self.clear)
        self.setting()

    def setting(self):
        self.combo.place(x=630, y=28)
        self.province_entry.place(x=80, y=28, width=140, height=25)
        self.city_entry.place(x=280, y=28, width=140, height=25)
        self.district_entry.place(x=480, y=28, width=140, height=25)
        self.address_entry.place(x=80, y=70, width=540, height=25)
        self.recipient_entry.place(x=80, y=118)
        self.contactnumber_entry.place(x=80, y=178)
        self.save_button.place(x=150, y=250, width=100, height=40)
        self.clear_button.place(x=430, y=250, width=100, height=40)
        return True

    @classmethod
    def open_current_directory(cls):
        current_directory = getcwd()
        system(f'explorer {current_directory}')

    def getting(self):
        return [[self.province_entry.get(), self.city_entry.get(), self.district_entry.get(), self.address_entry.get(),
                 self.recipient_entry.get(), self.contactnumber_entry.get(), self.combo.get()], self.entry_vars]

    def save(self):
        _gets = self.getting()[0]
        if all(_.strip() != "" for _ in _gets):
            with open('AddressSaveFile.txt', 'a', encoding='UTF-8') as file:
                file.write(
                    f'{_gets[0]}省{_gets[1]}市{_gets[2]}{_gets[6]}\t'
                    f'详细地址:{_gets[3]}\t收件人:{_gets[4]}\t联系电话:{_gets[5]}\n')
                messagebox.showinfo('Success', '保存成功')
        else:
            messagebox.showerror('Error', '请填写完整信息')

    def clear(self):
        self.active.set('')
        self.province_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.district_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.recipient_entry.delete(0, END)
        self.contactnumber_entry.delete(0, END)
        messagebox.showinfo('Success', '清除成功')

    def run(self):
        self.mainloop() if self.setting() else messagebox.showerror('Error', '初始化失败')

    def save_text(self, active=1):
        _gets = self.getting()[0]
        if all(_ == "" for _ in _gets):
            messagebox.showerror('Error', '请填写信息')
        else:
            with open('SavedText.txt', 'w', encoding='UTF-8') as file:
                for var in self.getting()[0]:
                    file.write(f'{var}')
                    if active <= len(self.getting()[1]):
                        file.write('\n')
                        active += 1
            messagebox.showinfo('Success', '保存当前数据成功')

    def load_text(self):
        try:
            with open('SavedText.txt', 'r', encoding='UTF-8') as file:
                lines = file.readlines()
                get_vars = self.getting()[1]
                for i, line in enumerate(lines):
                    get_vars[i].set(line.strip()) if i < len(get_vars) else self.active.set(lines[-1])

                messagebox.showinfo('Success', '加载数据成功')
        except FileNotFoundError:
            messagebox.showerror('Failed to load', '无保存的数据')


if __name__ == '__main__':
    win = DrawWindows(680, 320)
    win.run()
