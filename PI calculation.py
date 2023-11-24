def calculate_pi(precision):
    pi = 0
    for k in range(precision):
        pi += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))  # BBP公式
    print(pi)


while True:
    try:
        calculate_pi(int(input("请输入N的值：")))

    except ValueError:
        print("not a int")
    except KeyboardInterrupt:
        print("has been forcibly stopped")
