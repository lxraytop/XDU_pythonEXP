def sum_and_max(numbers):

    he = sum(numbers)
    zuidazhi = max(numbers)
    return he, zuidazhi


nums = input("输入数字列表，用空格分隔: ")
nums = [int(x) for x in nums.split()]
s, m = sum_and_max(nums)
print("和为：", s)
print("最大值为：", m)
