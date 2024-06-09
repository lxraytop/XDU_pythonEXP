import pickle

class Stack:
    def __init__(self):
        self.items = []

    def orempty(self):
        return len(self.items) == 0

    def add_stack(self, item):
        self.items.append(item)

    def pop(self):
        if not self.orempty():
            return self.items.pop()
        else:
            return None

    def top_stack(self):
        if not self.orempty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


s = Stack()
s.add_stack(1)
s.add_stack(2)
s.add_stack(3)

with open('stack.pkl', 'wb') as file:
    pickle.dump(s, file)

with open('stack.pkl', 'rb') as file:
    stack_new = pickle.load(file)

print("栈：")
while not stack_new.orempty():
    print(stack_new.pop())
