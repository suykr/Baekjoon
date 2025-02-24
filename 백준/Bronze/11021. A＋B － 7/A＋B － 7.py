import sys
 
x = int(input())
for i in range(1, x+1):
        a,b = map(int, input().split())
        print(f'Case #{i}: {a+b}')
