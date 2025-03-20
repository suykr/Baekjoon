l = []
res = []

for i in range(10):
    num = int(input())
    l.append(num)
    res.append(num%42)

res = list(set(res))
print(len(res))