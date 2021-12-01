def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans
N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
p=0
q=0
n=[1]*N
print(n)
fact=0
count=1
for i in P:
    fact=factorial(N-count)
    p=sum(n[0:i-1])*fact
    n[i-1]=0
    count+=1
n=[1]*N
count=1
for i in Q:
    fact=factorial(N-count)
    q=sum(n[0:i-1])*fact
    n[i-1]=0
    count+=1
print(abs(p-q))
