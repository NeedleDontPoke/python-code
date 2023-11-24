class ATMSystem:
    def __init__(self):
        self.accounts: dict = {}

    def reg(self, username, password):
        if username in self.accounts:
            print("用户名已存在，请使用其他用户名。")
        else:
            self.accounts[username] = {'password': password, 'balance': 0}
            print("注册成功，请登录。")

    def login(self, username, password):
        if username in self.accounts and self.accounts[username]['password'] == password:
            print("登录成功。")
            return True
        else:
            print("登录失败，请检查用户名和密码。")
            return False

    def check_balance(self, username):
        balance = self.accounts[username]['balance']
        print(f"您的余额为: {balance}")

    def deposit(self, username, amount):
        self.accounts[username]['balance'] += amount
        print(f"存款成功，当前余额为: {self.accounts[username]['balance']}")

    def withdraw(self, username, amount):
        if amount <= self.accounts[username]['balance']:
            self.accounts[username]['balance'] -= amount
            print(f"取款成功，当前余额为: {self.accounts[username]['balance']}")
        else:
            print("余额不足，取款失败。")

    def transfer(self, from_user, to_user, amount):
        if from_user in self.accounts and to_user in self.accounts:
            if amount <= self.accounts[from_user]['balance']:
                self.accounts[from_user]['balance'] -= amount
                self.accounts[to_user]['balance'] += amount
                print(f"转账成功，{from_user}的当前余额为: {self.accounts[from_user]['balance']}")
            else:
                print("余额不足，转账失败。")
        else:
            print("用户不存在，转账失败。")

    def main_menu(self):
        while True:
            print("\n请选择操作：")
            print("1. 注册")
            print("2. 登录")
            print("3. 退出")
            choice = input("请输入操作编号：")

            if choice == '1':
                while True:
                    username = input("请输入用户名: ")
                    if len(username) == 0:
                        print("用户名不能为空。")
                    elif ' ' in username:
                        print("用户名不能包含空格。")
                    else:
                        password = input("请输入密码: ")
                        if len(password) == 0:
                            print("密码不能为空。")
                        elif ' ' in password:
                            print("密码不能包含空格。")
                        else:
                            self.reg(username, password)
                            break
            elif choice == '2':
                username = input("请输入用户名: ")
                password = input("请输入密码: ")
                if self.login(username, password):
                    self.user_menu(username)
            elif choice == '3':
                print("欢迎下次再来。")
                break
            else:
                print("无效的操作，请重新选择。")

    def user_menu(self, username):
        while True:
            print("\n请选择操作：")
            print("1. 查询余额")
            print("2. 存款")
            print("3. 取款")
            print("4. 转账")
            print("5. 取卡")
            choice = input("请输入操作编号：")

            if choice == '1':
                self.check_balance(username)
            elif choice == '2':
                amount = float(input("请输入存款金额: "))
                self.deposit(username, amount)
            elif choice == '3':
                amount = float(input("请输入取款金额: "))
                self.withdraw(username, amount)
            elif choice == '4':
                to_user = input("请输入转账目标用户名: ")
                amount = float(input("请输入转账金额: "))
                self.transfer(username, to_user, amount)
            elif choice == '5':
                print("感谢使用ATM，取卡成功。")
                break
            else:
                print("无效的操作，请重新选择。")


if __name__ == "__main__":
    atm = ATMSystem()
    atm.main_menu()
