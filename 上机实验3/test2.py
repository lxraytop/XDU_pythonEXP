class Queue:
    def __init__(self):
        self.items = []

    def judge_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.judge_empty():
            return self.items.pop(0)
        else:
            return None  # 或者抛出一个异常

    def size(self):
        return len(self.items)


# 用户交互
q = Queue()
while True:
    print("----------------\n请选择操作：")
    print("1. 入队")
    print("2. 出队")
    print("3. 退出")
    choice = input("输入操作编号：")

    if choice == "1":
        item = input("入队数据：")
        q.enqueue(item)
        print(f"{item} 已入队")

    elif choice == "2":
        item = q.dequeue()
        if item is not None:
            print(f"出队的数据为：{item}")
        else:
            print("队列已空")

    elif choice == "3":
        break

    else:
        print("无效操作")
