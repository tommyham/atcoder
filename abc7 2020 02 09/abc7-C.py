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

    return over+same+under

N=int(input())
A=list(map(int,input().split()))
A=quick_sort(A)
ans="YES"
if(len(A)>1):
    for i in range(len(A)):
        if(A[i-1]==A[i]):
            ans="NO"
            break
        else:
            pass
else:
    pass
print(ans)