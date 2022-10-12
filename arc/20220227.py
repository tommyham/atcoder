def probA():    
    N=int(input())
    S=input()
    S=S.replace("A", "BB")
    S=S.replace("BB", "A")
    print(S)

N=int(input())
A=list(map(int, input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
if sum([abs(A[i]-B[i]) for i in range(N)]):
    print("No")
else:
    print("Yes")