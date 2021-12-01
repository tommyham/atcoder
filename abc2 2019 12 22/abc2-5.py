N=int(input())
count=0
ans=0
list=[]
while(N!=0):
    ans=N%10
    list.append(N%10)
    N=int(N/10)
    count+=1
print(list)
ans=0
way=0
for i in range(count):
    ans+=(way+i)*list[i]+i
    way+=(way+i)*9
    ans+=way
print(ans)
