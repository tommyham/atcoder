def probA():   
    V,A,B,C=map(int, input().split())
        
    i=0
    ans="F"
    while V>=0:
        if i%3==0:
            V-=A
            ans="F"
        elif i%3==1:
            V-=B
            ans="M"
        else:
            V-=C
            ans="T"
        i+=1                                                        
    print(ans)

def probB():
    N=int(input())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    hit,blow=0,0
    
    for i in range(N):
        if A[i]==B[i]:
            hit+=1
            continue
        for j in range(N):
            if A[i]==B[j]:
                blow+=1
                break
    print(hit)
    print(blow)

N=int(input())
query=list(list(map(int, input().split())) for _ in range(N))
S=input()

S=S.replace("R", "2")
S=S.replace("L", "0")
combine=[[query[idx][0],query[idx][1],s] for idx,s in enumerate(S)]

judge=False
for i in range(N):
    for j in range(i+1,N):
        if combine[i][1]==combine[j][1]:
            x1=combine[i][0]*(int(S[i])-1)
            x2=combine[j][0]*(int(S[j])-1)
            if x1+x2<0:
                judge=True
                break
    if judge:
        break
if judge:
    print("Yes")
else:
    print("No")
            