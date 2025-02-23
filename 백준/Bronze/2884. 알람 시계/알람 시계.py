a, b = map(int, input().split())
if a>=1:
    if b>=45:
        print(f'{a} {b-45}')
    elif b<45:
        print(f'{a-1} {b+15}')
elif a==0:
    if b>=45:
        print(f'{a} {b-45}')
    elif b<45:
        print(f'23 {b+15}')