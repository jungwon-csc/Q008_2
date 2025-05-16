
S = list(input())
n = len(S)
temp = S[0:1]

for i in range(n):
    for j in range(i, n):
        if S[i:j+1] == list(reversed(S[i:j+1])):
            if len(S[i:j+1]) > len(temp):
                temp = S[i:j+1]
print(*temp, sep='')
