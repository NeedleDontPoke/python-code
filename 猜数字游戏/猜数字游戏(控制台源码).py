import random  # 导入伪随机库

r = random.randint(1, 10)  # 变量r为伪随机的整数--int
while True:  # 一个循环
    try:  # 尝试运行
        u = int(input("输入你猜的数字(1-10):"))  # 用一个变量u存储用户输入的规定范围内的整数
        if u == r:  # 判断用户如数的数字r是否等于伪随机数r
            print("你猜对了")  # 如果等于，则打印猜对了
            break  # 退出程序(循环)
        elif u > 10 or u < 1:  # 判断是否超出范围
            print("你猜的数字超出了1-10的范围")  # 打印超出范围
        elif u > r:
            print("你猜大了")
        else:
            print("你猜小了")
    except ValueError:
        print("请输入数字")  # 打印
