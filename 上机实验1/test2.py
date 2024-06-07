import random

randnum = [random.randint(1, 100) for _ in range(20)]
randnum[:10] = sorted(randnum[:10])
randnum[10:] = sorted(randnum[10:], reverse=True)

print("列表:", randnum)
