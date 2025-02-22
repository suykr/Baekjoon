a = int(input())
b = input()
l = list(b)
l.reverse()
res = 0
asdf = 0
for i in l:
    print(a*int(i))
    res+= a*int(i)*(10**asdf)
    asdf += 1
print(res)