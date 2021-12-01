def factorial(N):
    fact=[]
    ans=1
    fact.append(ans)
    for i in range(1,N+1):
        ans=ans*i
        fact.append(i)
    return fact

def cmb(N,K,F):
    cmbi=[]
    ans=1
    for i in range(N):
        ans=F[i]/(F[K]*F[i-K])
        combi.append(ans)
    return combi

def quick_sort(list):
    stand=list[0]
    over=[]
    same=[]
    under=[]
    for i in list:
        if(i>stand):
            over.append(i)
        elif(i<stand):
            under.append(i)
        else:
            same.append(i)
    if(len(over)>1):
        over=quick_sort(over)
    else:
        pass
    if(len(under)>1):
        under=quick_sort(under)
    else:
        pass
    return over+same+under
N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=0
A=quick_sort(A)
c=1
count=0
maxim=0
mini=0
mod=10**9+7
fact=factorial(N)
combi=cmb(N-1,K-1,fact)
if(K>1):
    for i in range(K-2,N-2):
        for j in range(i+K-1,N):
            if(count!=0):
                c=c*(j-i-1)/(j-i-1-(K-2))
                ans+=(A[i]-A[j])*c
            else:
                ans+=(A[i]-A[j])*c
            count+=1
        c=1
        count=0
else:
    pass
print(int(ans%mod))