def count_types(string):
    upper = 0
    lower = 0
    digit = 0
    other = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        else:
            other += 1
    counts = (upper, lower, digit, other)
    return counts


string = input("输入字符串: ")
count = count_types(string)
print("大写字母数目:", count[0])
print("小写字母数目:", count[1])
print("数字数目:", count[2])
print("其他字符数目:", count[3])
