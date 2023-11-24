import tkinter as tk
import tkinter.ttk as ttk
import csv

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("表格数据")

        self.load_button = tk.Button(
            self.master, text="加载数据", command=self.load_data)
        self.load_button.pack()

    def load_data(self):
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            data = list(reader)

        columns = data[0]
        rows = data[1:]

        self.treeview = ttk.Treeview(self.master, columns=columns, show="headings")

        for column in columns:
            self.treeview.heading(column, text=column)

        for row in rows:
            self.treeview.insert("", tk.END, values=row)

        self.treeview.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
