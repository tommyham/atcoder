def probA():
    Y=int(input())
    
    s=Y%4
    if s==2:
        print(Y)
    elif s>2:
        print(Y+s)
    else:
        print(Y+(2-s))

def probB():
    N,M=map(int, input().split())
    road=[[False]*(N) for _ in range(N)]
    
    for _ in range(M):
        u,v=map(int, input().split())
        road[u-1][v-1]=True
        road[v-1][u-1]=True
    
    ans=0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if road[i][j] and road[j][k] and road[k][i]:
                    ans+=1
    
    print(ans)
def probC():
    N=int(input())
    A=list(map(int, input().split()))
    
    ans=0
    match=0
    for i in range(N):
        if A[i]==i+1:
            match+=1
        elif A[A[i]-1]==i+1:
            if A[i]-1<i:
                pass
            else:
                ans+=1
    
    print(ans+int(match*(match-1)/2))

def main():
    N=int(input())
    A=list(map(int, input().split()))
    
    divisor=998244353
    ans=0
    
    # from functools import lru_cache
    
    # @lru_cache(maxsize=1000)
    def choice(num_list,n,S=[]):
        judge=0
        for i in range(len(num_list)):
            S.append(num_list[i])
            if n!=1:
                judge+=choice(num_list[i+1:],n-1,S)
            else:
                if not sum(S)%len(S):
                    judge+=1
                else:
                    pass
            S.pop(-1)
        
        return judge
    
    for i in range(N):
        ans+=choice(A, i+1)
    print(ans%divisor)

if __name__ == '__main__':
    main()