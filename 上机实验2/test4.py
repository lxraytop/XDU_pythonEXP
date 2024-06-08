class TXL:
    def __init__(self):
        self.contacts = {}

    def add_txl(self, name, phone, email, company):
        self.contacts[name] = {'phone': phone, 'email': email, 'company': company}

    def delete_txl(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} 的信息已删除")
        else:
            print(f"{name} 不存在")

    def search_txl(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"姓名: {name}, 电话: {info['phone']}, 邮箱: {info['email']}, 单位: {info['company']}")
        else:
            print(f"{name} 不存在")

    def display_txls(self):
        print("通讯录内容：")
        for name, info in self.contacts.items():
            print(f"姓名: {name}, 电话: {info['phone']}, 邮箱: {info['email']}, 单位: {info['company']}")


# 创建通讯录对象
contact_book = TXL()

# 用户交互
while True:
    print("-------------------\n请选择操作：")
    print("1. 添加通讯人")
    print("2. 删除通讯人")
    print("3. 查询通讯人信息")
    print("4. 输出所有通讯录信息")
    print("5. 退出")
    choice = input("输入操作编号：")

    if choice == "1":
        name = input("输入姓名：")
        phone = input("输入电话：")
        email = input("输入邮箱：")
        company = input("输入单位：")
        contact_book.add_txl(name, phone, email, company)
        print(f"{name} 的信息已添加")

    elif choice == "2":
        name = input("输入要删除的姓名：")
        contact_book.delete_txl(name)

    elif choice == "3":
        name = input("输入要查询的姓名：")
        contact_book.search_txl(name)

    elif choice == "4":
        contact_book.display_txls()

    elif choice == "5":
        print("退出通讯录")
        break

    else:
        print("无效操作，请重新输入")
