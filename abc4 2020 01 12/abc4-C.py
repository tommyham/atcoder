N,M=map(int,input().split())
P=[0]*M
S=[0]*M
cor=[0]*N
ac,wa=0,0
for i in range(M):
    P[i],S[i]=input().split()
    P[i]=int(P[i])
    if(S[i]=="AC"):
        cor[P[i]-1]+=1
    else:
        pass
for i in range(M):
    if(cor[P[i]-1]>=1 and S[i]=="WA"):
        wa+=1
    elif(cor[P[i]-1]>=1 and S[i]=="AC"):
        cor[P[i]-1]=0
        ac+=1
    else:
        pass
print("{0} {1}".format(ac,wa))