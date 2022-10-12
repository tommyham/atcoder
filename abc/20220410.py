def probA():    
    S=input()
    S=S[:-1]
    S="0"+S
    print(S)

N=int(input())
query=[list(map(int, input().split()))for _ in range(N)]
judge=True

for i in range(len(query)):
    for j in range(len(query[i:])):
        if query[i][0]==query[j][0] and query[i][1]==query[j][0]:
            judge=False
            break
        else:
            pass
    if judge:
        pass
    else:
        break
if judge:
    print("Yes")
else:
    print("No")