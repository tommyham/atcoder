def maxim(S,N,M,A,j,ans):
    way=0
    for i in range(j,M+1):
        A.append(i)
        #print(A)
        if(len(A)==N):
            #print(A)
            for k in S:
                #print(k)
                if(A[k[1]-1]-A[k[0]-1]==k[2]):
                    way+=k[3]
                else:
                    pass
                #print(way)
            if(way>ans):
                ans=way
            else:
                pass
            way=0
            #print(ans)
        else:
            way=maxim(S,N,M,A,i,ans)
            #print(way)
            #print(A)
            if(way>ans):
                ans=way
            else:
                pass
            way=0
        A.pop(len(A)-1)
        #print(A)
    return ans

N,M,Q=map(int,input().split())
S=[]
A=[]
for i in range(Q):
    S.append(list(map(int,input().split())))
ans=0
ans=maxim(S,N,M,A,1,ans)
print(ans)