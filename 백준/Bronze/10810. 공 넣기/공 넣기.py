N, M =map(int, input().split())
backet = []
for i in range(N):
    backet.append(0)

for i in range(M):
    i, j, k = map(int, input().split())
    backet[i-1:j] = [k] * (j-i+1)

print(' '.join(list(map(str, backet))))