a, b = map(int, input().split())
c = int(input())

if b+c>=60:
    count = (b+c)//60
    left = (b+c)%60
    a+=count
    if a>=24:
        print(f'{a%24} {left}')
    elif a<24:
        print(f'{a} {left}')
elif b+c<60:
    count = (b+c)//60
    a+=count
    if a>=24:
        print(f'{a%24} {b+c}')
    elif a<24:
        print(f'{a} {b+c}')