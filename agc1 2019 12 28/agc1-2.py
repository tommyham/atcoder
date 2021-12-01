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

N,M,V,P=map(int,input().split())
A=list(map(int,input().split()))
A=quick_sort(A)
print(A)
count=0
if(P>=V):
    for i in range(N):
        if(A[N-1-i]+M>=A[P-1]):
            count=len(A)-i
            break
        else:
            pass
else:
    for i in range(N):
        print("{0},{1},{2}".format(A[N-1-i],A[P-1],A[N-V+P-1]))
        if(A[N-1-i]+M>=A[P-1] and A[N-V+P-1]==A[N-1-i]):
            count=len(A)-i
            break
        else:
            pass
print(int(count))