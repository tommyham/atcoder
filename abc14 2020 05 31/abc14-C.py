A,B=map(float,input().split())
ans=A*B
ans=str(ans)
count=-1
for i in reversed(ans):
    if(i=="."):
        break
    else:
        count-=1
ans=int(ans[:count])
print(ans)