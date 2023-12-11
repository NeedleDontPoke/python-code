import sys
import tkinter as tk
from tkinter import messagebox

from numpy import random

import FileFixer


def show_fix_option(filename):
    fixer = FileFixer.FixFile(filename)
    result = messagebox.askquestion('File Missing', 'File missing, fix or not')
    if result == 'yes' and fixer.fix():
        messagebox.showinfo('Successful Fix', 'The program need to restart')
    sys.exit()


def load_word_list(filename):
    fixer = FileFixer.FixFile(filename)
    # 从文件中加载单词列表
    try:
        with open(filename, 'r') as file:
            get = [line.strip() for line in file]
            return get if get == fixer.get_list(filename) else show_fix_option(filename)
    except FileNotFoundError:
        show_fix_option(filename)


def choose_game_mode(choice):
    # 选择游戏难度模式，返回对应的文件名和生命值
    modes = {'easy': ('word_list_easy.txt', 5), 'hard': ('word_list_hard.txt', 3), 'dead': ('word_list_dead.txt', 1)}
    return modes.get(choice)


class GameDifficultyWindow:
    def __init__(self, master):
        # 游戏设置界面的控件
        self.master = master
        self.master.title("Difficulty Selection")
        window_width = 300
        window_height = 180
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.master.minsize(window_width, window_height)
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")
        tk.Label(master, text="Select Game Difficulty").pack(pady=10)
        tk.Radiobutton(master, text="Easy", variable=self.difficulty_var, value="easy", fg="green").pack()
        tk.Radiobutton(master, text="Hard", variable=self.difficulty_var, value="hard", fg="red").pack()
        tk.Radiobutton(master, text="Dead", variable=self.difficulty_var, value="dead", fg="purple").pack()
        tk.Button(master, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        difficulty_choice = self.difficulty_var.get()
        self.master.destroy()
        GameWindow(difficulty_choice)


class WordMemory:
    def __init__(self, document, live):
        # 初始化游戏对象
        self.__document = document  # 总单词列表
        self.point = 0  # 分数
        self.live = live  # 生命值
        self.words_seen = set()  # 用于存放已经出现过的单词
        self.last_word = None  # 用于存放上一次出现的单词

    def r_len(self):
        return len(self.words_seen) == len(self.__document)

    def r_point(self):
        return self.point

    def r_live(self):
        return self.live

    def display_word(self):
        # 65%的概率从没有出现过的单词中随机生成单词，35%的概率从words_seen中随机生成单词
        while True:
            if not self.words_seen or random.choice([True, False], p=[0.65, 0.35]):
                # 从没有出现过的单词中随机选择一个单词，确保不同于上一次显示的单词
                available_words = [word for word in self.__document if
                                   word not in self.words_seen and word != self.last_word]
            else:
                # 从已经出现过的单词中随机选择一个单词，确保不同于上一次显示的单词
                available_words = self.words_seen.copy()
                if self.last_word is not None:
                    available_words.discard(self.last_word)
            if available_words:
                selected_element = random.choice(list(available_words))
                if selected_element != self.last_word:
                    self.last_word = selected_element
                    return selected_element

    def judge(self, choice, word):
        # 判断用户的选择是否正确，更新分数、生命值和单词状态
        if (word not in self.words_seen and choice == 'new') or (word in self.words_seen and choice == 'seen'):
            self.point += 1
        else:
            self.live -= 1
        self.words_seen.add(word)  # 出现过的单词放入集合里


class GameWindow:
    def __init__(self, difficulty):
        # 设置游戏界面的控件
        self.root = tk.Tk()
        self.root.title("Word Memory Game")
        window_width = 300
        window_height = 150
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.minsize(window_width, window_height)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.mode_filename, self.lives = choose_game_mode(difficulty)
        self.word_list = load_word_list(self.mode_filename)
        self.word_memory = WordMemory(self.word_list, self.lives)
        self.menubar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label='Menu', command=self.go_home_page)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Current Difficulty',
                                   command=lambda: messagebox.showinfo("Difficulty", f"Difficulty:{difficulty}"))
        self.menubar.add_cascade(label='option', menu=self.file_menu)
        self.root.config(menu=self.menubar)
        self.word_label = tk.Label(self.root, font=('Arial', 15))
        self.word_label.pack(pady=10)
        self.choice_var = tk.StringVar()
        self.choice_var.set("new")
        tk.Radiobutton(self.root, text="New", variable=self.choice_var, value="new").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(self.root, text="Seen", variable=self.choice_var, value="seen").pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Submit", command=self.submit_choice).pack(pady=10)
        self.score_label = tk.Label(self.root)
        self.score_label.pack()
        self.live_label = tk.Label(self.root, text=f"Lives: {self.lives}")
        self.live_label.pack()
        self.word = self.word_memory.display_word()
        self.update_game_info()
        self.run_game()

    def submit_choice(self):
        # 处理事件
        self.word_memory.judge(self.choice_var.get(), self.word)
        self.word = self.word_memory.display_word()
        self.update_game_info()

    def update_game_info(self):
        # 更新游戏信息
        self.word_label.config(text=f'Word: {self.word}', font=('Arial', 15))
        self.score_label.config(text=f"Score: {self.word_memory.r_point()}")
        self.live_label.config(text=f"Lives: {self.word_memory.r_live()}")
        if self.word_memory.r_len():
            messagebox.showinfo("Game Victory", f"Game Victory. Your score is {self.word_memory.point}")
            self.go_home_page()
        elif self.word_memory.r_live() == 0:
            messagebox.showinfo("Game Over", f"Game Over. Your score is {self.word_memory.point}")
            self.go_home_page()

    def go_home_page(self):
        self.root.destroy()
        run()

    def run_game(self):
        self.root.protocol("WM_DELETE_WINDOW", self.go_home_page)
        self.root.mainloop()


def run():
    difficulty_window = tk.Tk()
    GameDifficultyWindow(difficulty_window)
    difficulty_window.mainloop()


if __name__ == '__main__':
    run()
