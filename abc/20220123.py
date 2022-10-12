def probA():
    S=list(input())
    a,b=map(int,input().split())
    S_a=S[a-1]
    S_b=S[b-1]
    S[a-1]=S_b
    S[b-1]=S_a
    print(*S,sep="")

def probB():
    N=int(input())
    A=list(map(int,input().split()))
    total=int(4*(N+1)*N/2)
    print(total-sum(A))

def probC():
    N,M=map(int,input().split())
    S=list(map(str, input().split()))
    T=list(map(str, input().split()))
    s=0
    for t in T:
       while True:
           if t==S[s]:
               s+=1
               print("Yes")
               break
           else:
               s+=1
               print("No")
 
import numpy as np
N=2
A=[[4, 0, 1], [5, 3], [2]]
# bin_A=[[bin(i).replace('0b', '') for i in a]for a in A]
ans=0