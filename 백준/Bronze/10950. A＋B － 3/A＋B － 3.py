case = int(input())
res = ''
for i in range(1, case+1):
    a, b = map(int, input().split())
    res += str(a+b)+'\n'
print(res)