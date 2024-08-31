def probA():
    N,T,A=map(int,input().split())

    if abs(T-A)>(N-(T+A)):
        print("Yes")
    else:
        print("No")

def probB():
    N=int(input())
    S=[]
    M=0
    for _ in range(N):
        S.append(input())
        if len(S[-1])>M:
            M=len(S[-1])
    T=["" for _ in range(M)]
    for s in S:
        for i in range(len(T)):
            if len(s)>i:
                T[i]=s[i]+T[i]
            else:
                if len(T[i])>=1:
                    T[i]="*"+T[i]
    
    for t in T:
        print(t)

def probC():
    Q=int(input())

    count=0
    num={}
    for _ in range(Q):
        query=list(map(int,input().split()))

        if query[0]==1:
            if query[1] in num:
                num[query[1]]+=1
            else:
                num[query[1]]=1
                count+=1
        elif query[0]==2:
            if num[query[1]]==1:
                count-=1
                num.pop(query[1])
            else:
                num[query[1]]-=1
        else:
            print(count)


def main():
    N=int(input())
    A=[[list(map(int,input().split())) for _ in range(N)] for _ in range(N)]
    sum=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                sum[i+1][j+1][k+1]=sum[i][j+1][k+1]+sum[i+1][j][k+1]+sum[i+1][j+1][k]


    Q=int(input())
    
    ans=[]
    for _ in range(Q):
        lx,rx,ly,ry,lz,rz=map(int,input().split())
        tmp=0
        Ax=A[lx-1:rx]
        for ax in Ax:
            Ay=ax[ly-1:ry]
            for ay in Ay:
                for z in ay[lz-1:rz]:
                    tmp+=z
        ans.append(tmp)
    
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()