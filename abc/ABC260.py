def probB():
    N,X,Y,Z=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    
    ALL=[A[i]+B[i] for i in range(len(A))]
    num=[i for i in range(1,N+1)]
    query=[[A[i],B[i],ALL[i],num[i]] for i in range(N)]
    ans=[]
    
    query=sorted(query, key=lambda x:(x[0]),reverse=True)
    ans+=[query[i][3] for i in range(min(X,len(query)))]
    query=query[X:]
    query=sorted(query, key=lambda x:(x[3]))
    
    query=sorted(query, key=lambda x:(x[1]),reverse=True)
    ans+=[query[i][3] for i in range(min(Y,len(query)))]
    query=query[Y:]
    query=sorted(query, key=lambda x:(x[3]))
    
    query=sorted(query, key=lambda x:(x[2]),reverse=True)
    ans+=[query[i][3] for i in range(min(Z,len(query)))]
    query=query[Z:]
    
    ans.sort()
    for n in ans:
      print(n)

N,X,Y=map(int, input().split())
