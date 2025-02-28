l = []
for i in range(1, 9+1):
    l.append(int(input()))
print(f'{max(l)}\n{l.index(max(l))+1}')