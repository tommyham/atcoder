N=int(input())
A=list(map(int,input().split()))
count=0
while(len(A)!=count):
    if(A[count]%2==0):
        pass
    else:
        A.pop(count)
        count=-1
    count+=1
ans="APPROVED"
for i in A:
    if(i%3==0 or i%5==0):
        pass
    else:
        ans="DENIED"
        break
print(ans)