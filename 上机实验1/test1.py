import random

count = {}

for _ in range(1000):
    num = random.randint(0, 100)
    count[num] = count.get(num, 0) + 1

for num, counts in count.items():
    print(f"数字 {num} 出现了 {counts} 次")
