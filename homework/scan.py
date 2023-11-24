import tkinter
import random

# 定义窗口
window = tkinter.Tk()
window.title('猜数字游戏')
window.geometry('400x200')
# 生成一个1-100之间的随机数
number = random.randint(1, 100)
# 用户猜测的次数
guess_times = 0


# 定义函数
def guess_number():
    global guess_times
    guess_times += 1
    guess_number = int(number_input.get())
    if guess_number > number:
        result_label.config(text='你猜的数字大了！')
    elif guess_number < number:
        result_label.config(text='你猜的数字小了！')
    else:
        result_label.config(text='恭喜你，猜对了！')
        result_label.config(text='你一共猜了{}次'.format(guess_times))


# 创建标签
number_label = tkinter.Label(window, text='请输入你猜的数字：')
number_label.pack()
# 创建输入框
number_input = tkinter.Entry(window)
number_input.pack()
# 创建按钮
guess_button = tkinter.Button(window, text='猜数字', command=guess_number)
guess_button.pack()
# 创建结果标签
result_label = tkinter.Label(window, text='')
result_label.pack()
# 运行窗口
window.mainloop()
