def probA():
    N=int(input())
    if (N>=2**31) or (N<-(2**31)):
        print("No")
    else:
        print("Yes")

def probB():
    H,W=map(int, input().split())
    A=[list(map(int, input().split())) for _ in range(H)]
    
    for i in range(W):
        col=[0]*(H)
        for j in range(H):
            col[j]=A[j][i]
        print(*col,sep=" ")

S=input()
size=len(S)
for _ in range(size):
    judge=True
    length=int(len(S)/2)
    for i in range(length):
        if S[i]==S[-(i+1)]:
            pass
        else:
            judge=False
            break
    if judge:
        break
    else:
        S="a"+S
        pass
if judge:
    print("Yes")
else:
    print("No")