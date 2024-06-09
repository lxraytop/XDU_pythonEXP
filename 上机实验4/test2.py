class Details:
    def __init__(self):
        self.__name = ''

    def setDetails(self):
        self.__name = input("输入名字：")

    def showDetails(self):
        print("名字:", self.__name)


class Employee(Details):
    def __init__(self):
        super().__init__()
        self.__company = ''

    def setEmployee(self):
        self.__company = input("输入公司名字：")

    def showEmployee(self):
        self.showDetails()
        print("公司名字:", self.__company)


co = Employee()

co.setDetails()
co.setEmployee()
co.showEmployee()
