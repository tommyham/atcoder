def probA():
    N=int(input())
    digit=N//4
    N=N%4
    if N:
        X=str(N)+str(4)*digit
    else:
        X=str(4)*digit
    M=0
    for x in X:
        M+=2*int(x)
    print(M)
    print(X)

N,a,b=6,123,321
A=[10, 100, 1000, 10000, 100000, 1000000]

N,a,b=map(int, input().split())
A=list(map(int, input().split()))

boundary=min(A)+1
up_bound=sum(A)/(len(A))
ans=min(A)

A_high=[(a_-boundary)//b for a_ in A if a_>=boundary]
A_low=[(boundary-a_)//a if not (boundary-a_)%a else (boundary-a_)//a+1 for a_ in A if a_<boundary]

high_surplus=[(a_-boundary)%b for a_ in A if a_>=boundary]
low_surplus=[a-(boundary-a_)%a for a_ in A if a_<boundary]

while boundary<=up_bound:
    
    if sum(A_high)>=sum(A_low):
        pass
    else:
        break
    boundary+=min(min(high_surplus),min(low_surplus))+1
print(boundary-1)
