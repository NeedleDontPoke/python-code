import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib


def create_table():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()


def hash_password(password):
    # 使用SHA-256进行密码哈希
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def register():
    username = username_entry.get()
    password = password_entry.get()
    username_active.set('')
    password_active.set('')
    if not username or not password:
        messagebox.showerror("Error", "用户名和密码不能为空")
        return

    hashed_password = hash_password(password)

    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # 检查用户名是否已存在
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone():
        messagebox.showerror("Error", "用户名已存在")
        conn.close()
        return

    # 注册用户
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "注册成功")


def login():
    username = username_entry.get()
    password = password_entry.get()
    username_active.set('')
    password_active.set('')
    if not username or not password:
        messagebox.showerror("Error", "用户名和密码不能为空")
        return

    hashed_password = hash_password(password)

    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # 验证用户
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    if cursor.fetchone():
        messagebox.showinfo("Success", "登录成功")
    else:
        messagebox.showerror("Error", "用户名或密码错误")

    conn.close()


# 创建用户数据表
create_table()

# 创建GUI窗口
width = 210
height = 100
root = tk.Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
root.resizable(False, False)
root.title("登录注册界面")

username_active = tk.StringVar()
password_active = tk.StringVar()
# 用户名和密码输入框
tk.Label(root, text="用户名").grid(row=0, column=0)
username_entry = tk.Entry(root, textvariable=username_active)
username_entry.grid(row=0, column=1)

tk.Label(root, text="密码").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*", textvariable=password_active)
password_entry.grid(row=1, column=1)

# 注册和登录按钮
register_button = tk.Button(root, text="注册", command=register)
register_button.place(x=40, y=55)

login_button = tk.Button(root, text="登录", command=login)
login_button.place(x=140, y=55)

root.mainloop()
