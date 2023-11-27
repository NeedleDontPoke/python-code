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
        Label(self, font=('宋体', 12), text='地址:').place(x=20, y=30)
        Label(self, font=('宋体', 12), text='省').place(x=240, y=30)
        Label(self, font=('宋体', 12), text='市').place(x=440, y=30)
        Label(self, font=('宋体', 12), text='收件人:').place(x=10, y=120)
        Label(self, font=('宋体', 12), text='联系电话:').place(x=2, y=180)
        self.active = StringVar()
        self.combo = Combobox(self, font=('宋体', 14), width=2, textvariable=self.active)
        self.combo['value'] = ('区', '县')
        self.combo['state'] = 'readonly'
        self.province_entry = Entry(self, font=('楷体', 15))
        self.city_entry = Entry(self, font=('楷体', 15))
        self.district_entry = Entry(self, font=('楷体', 15))
        self.address_entry = Entry(self, font=('楷体', 15))
        self.recipient_entry = Entry(self, font=('楷体', 15))
        self.contactnumber_entry = Entry(self, font=('楷体', 15))
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

    def save(self):
        _gets = [self.province_entry.get(), self.city_entry.get(), self.district_entry.get(), self.combo.get(),
                 self.address_entry.get(), self.recipient_entry.get(), self.contactnumber_entry.get()]
        if all(_.strip() != "" for _ in _gets):
            with open('AddressSaveFile.txt', 'a', encoding='UTF-8') as file:
                file.write(
                    f'{_gets[0]}省{_gets[1]}市{_gets[2]}{_gets[3]}\t详细地址:{_gets[4]}\t收件人:{_gets[5]}\t联系电话:{_gets[6]}\n')
                file.close()
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


if __name__ == '__main__':
    win = DrawWindows(680, 320)
    win.run()
