n=int(input())
R=list(map(int,input().split()))
C=list(map(int,input().split()))
q=int(input())
r,c=[],[]
for i in range(q):
    temp=list(map(int,input().split()))
    r.append(temp[0])
    c.append(temp[1])
print(n)
print(R)
print(C)
print(q)
print(r,c)
