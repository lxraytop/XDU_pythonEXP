def sortray(arr, key=None, reverse=False):
    def compare(x):
        return x if key is None else key(x)

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (not reverse and compare(arr[j]) > compare(arr[j + 1])) or (
                    reverse and compare(arr[j]) < compare(arr[j + 1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


nums = input("输入数字列表，用空格分隔: ")
nums = [int(x) for x in nums.split()]
print("排序前：", nums)
nums = sortray(nums, reverse=True)
print("排序后：", nums)
