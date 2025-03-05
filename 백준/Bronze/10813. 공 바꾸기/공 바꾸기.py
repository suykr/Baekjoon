N, M = input().split()
backet = []
for i in range(int(N)):
    backet.append(str(i+1))
for i in range(int(M)):
    i, j = map(int, input().split())
    backet[i-1], backet[j-1] = backet[j-1], backet[i-1]

print(' '.join(backet))