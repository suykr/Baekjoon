x = int(input())
N = int(input())
all = 0
for i in range(1, N+1):
    a, b = map(int, input().split())
    all += a*b
if x == all:
    print('Yes')
else:
    print('No')
