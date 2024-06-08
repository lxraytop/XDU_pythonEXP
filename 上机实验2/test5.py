def judge_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sumsum(start, end):
    sumsum = 0
    for num in range(max(2, start), end + 1):
        if judge_num(num):
            sumsum += num
            yield num
    print(f"{start} 到 {end} 内的质数和为: {sumsum}")


a = int(input("开始于："))
b = int(input("结束于："))

for i in sumsum(a, b):
    print(i)
