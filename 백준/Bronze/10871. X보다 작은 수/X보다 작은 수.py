N, X = map(int, input().split())
list = input().split()
res = ''
for a in list:
    if int(a)<X:
        res+=a+' '
print(res)