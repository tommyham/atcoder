def probA():
    S=str(input())
    print(S[len(S)//2])

def probB():
    N=int(input())
    print(N%998244353)

vertex=[list(map(int, input().split())) for _ in range(4)]

index=0
for i in range(1,len(vertex)):
    if vertex[index][1]>vertex[i][1]:
        index=i
    else:
        pass

vertex=vertex[index:len(vertex)]+vertex[:index]

# angle=0
# count=0
# while angle<180 or count<3:
    
