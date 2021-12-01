N=int(input())
n=list(input().split())
mini=N
print(n)
count=0
k=0
while count>=0:
    way=len(n)
    for i in range(len(n)):
        if way-1>=i:
            print(i)
            k=int(n[i])
            if k<i+1:
                pass
            else:
                del(n[i])
                count+=1
    if count>0:
        count=0
    else:
        break
print(n)
if count>0:
    print(mini)
else:
    print(-1)
