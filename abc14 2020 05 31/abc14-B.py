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

    return under+same+over

N=int(input())
A=list(map(int,input().split()))
A=quick_sort(A)
ans=1
way=0
for i in A:
    ans*=i
    way=str(ans-1)
    if(len(way)>=19):
        ans=-1
        break
    else:
        pass
print(ans)