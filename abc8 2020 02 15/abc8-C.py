def com_str(A,B,i):
    ans=A
    if(A==B):
        pass
    elif(ord(A[i])>ord(B[i])):
        pass
    elif(ord(B[i])>ord(A[i])):
        ans=B
    else:
        ans=com_str(A,B,i+1)
    return ans

def quick_sort_str(list,N):
    stand=list[0]
    over=[]
    same=[]
    under=[]
    for i in list:
        if(i[N]!=stand[N]):
            if(stand[N]==com_str(i[N],stand[N],0)):
                over.append(i)
            else:
                under.append(i)
        else:
            same.append(i)
    if(len(over)>1):
        over=quick_sort_str(over,N)
    else:
        pass
    if(len(under)>1):
        under=quick_sort_str(under,N)
    else:
        way=[same[0][0],len(same)]
        same.clear()
        same.append(way)
    return over+same+under

def quick_sort_num(list,N):
    stand=list[0]
    over=[]
    same=[]
    under=[]
    for i in list:
        if(i[N]>stand[N]):
            over.append(i)
        elif(i[N]<stand[N]):
            under.append(i)
        else:
            same.append(i)
    if(len(over)>1):
        over=quick_sort_num(over,N)
    else:
        pass
    if(len(under)>1):
        under=quick_sort_num(under,N)
    else:
        pass

    return over+same+under

N=int(input())
S=[[] for i in range(N)]
for i in range(N):
    S[i].append(str(input()))
    S[i].append(1)
S=quick_sort_str(S,0)
S=quick_sort_num(S,1)
count=S[0][1]
for i in range(len(S)):
    if(S[i][1]==count):
        print(S[i][0])
    else:
        break