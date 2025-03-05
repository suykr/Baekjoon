l = list(range(1, 31))
for i in range(1, 29):
    l.remove(int(input()))

print('\n'.join(list(map(str, l))))