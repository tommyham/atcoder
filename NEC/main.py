def probA():
    S1=input().split()
    S2=input().split()
    S1=list(S1[0])
    S2=list(S2[0])
    
    if(S1[0]=="#"):
       if(S1[0]==S1[1] or S1[0]==S2[0]):
           print("Yes")
       else:
           print("No")
    else:
       if(S2[1]=="#"):
          print("Yes")
       else:
          print("No")

def probB():
    A,B=map(int,input().split())
    A=list(str(A))
    B=list(str(B))
    if(len(A)>len(B)):
        B=["0" for i in range(len(A)-len(B))]+B
    elif(len(B)>len(A)):
        A=["0" for i in range(len(B)-len(A))]+A
    result=list(map(lambda x,y:int(x)+int(y),A,B))
    answer=[True if i<10 else False for i in result]
    if(False in answer):
        print("Hard")
    else:
        print("Easy")

def probC():
    N,W=map(int,input().split())
    AB=[map(int,input().split()) for _ in range(N)]
    A,B=[list(i)for i in zip(*AB)]
    zipList=zip(A,B)
    zipSort=sorted(zipList,reverse=True)
    A,B=zip(*zipSort)
    answer=0
    for i in range(len(A)):
        if(B[i]<=W):
            W-=B[i]
            answer+=A[i]*B[i]
        else:
            answer+=W*A[i]
            break
    print(answer)

def probD():
    S=input().split()
    S=list(S[0])
    K=input().split()
    K=int(K[0])
    r=0
    ans=0
    for l in range(len(S)):
        while r<len(S) and (K or S[r]=="X"):
            if(S[r]=="."):
                K-=1
            r+=1
        ans=max(ans,r-l)
        if(S[l]=="."):
            K+=1
    print(ans)

class unionfind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

N,M=map(int,input().split())
path=[[] for _ in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    path[a-1].append(b-1)
ans=0
uf=unionfind(N)
ans2=[0]*N
for i in range(N-1,-1,-1):
    ans2[i]=ans
    ans+=1
    for j in path[i]:
        a,b=uf.find(i),uf.find(j)
        if a!=b:
            uf.union(i,j)
            ans-=1
for i in ans2:
    print(i)