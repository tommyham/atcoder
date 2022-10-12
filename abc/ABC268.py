def probA():
    num=set(map(int, input().split()))
    print(len(num))

def probB():
    S=str(input())
    T=str(input())
    
    if len(S)>len(T):
        print('No')
    else:
        if T[:len(S)]==S:
            print('Yes')
        else:
            print('No')

N=int(input())
P=list(map(int, input().split()))

ans=0
for i in range(N):
    count=0
    start=i
    for p in range(P):
        if start==p-1 or start==p+1:
            count+=1
        else:
            if ans<count:
                ans=count
            else:
                count=0