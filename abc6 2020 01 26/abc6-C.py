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

N,K=map(int,input().split())
H=list(map(int,input().split()))
H=quick_sort(H)
if(N<=K):
    print(0)
else:
    print(sum(H[K:N]))