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

def buble_sort(list):
    i=len(list)
    while(i>1):
        for j in range(i-1):
            if(list[j]<list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
            else:
                pass
        i-=1
    return list

def shaker_sort(list):
    i=len(list)
    j=0
    while(i>j):
        for k in range(j,i-1):
            if(list[k]<list[k+1]):
                list[k],list[k+1]=list[k+1],list[k]
            else:
                pass
        i-=1
        for k in reversed(range(j+1,i)):
            if(list[k]>list[k-1]):
                list[k],list[k-1]=list[k-1],list[k]
            else:
                pass
        j+=1
    return list

def comb_sort(list):
    h=int(len(list)//1.3)
    while(h!=1):
        for i in range(len(list)-h-1):
            if(list[i]<list[i+h]):
                list[i],list[i+h]=list[i+h],list[i]
            else:
                pass
        h=int(h//1.3)
    return list

def select_sort(list):
    maxim=0
    for i in range(len(list)):
        maxim=i
        for j in range(i,len(list)):
            if(list[maxim]<list[j]):
                maxim=j
            else:
                pass
        list[maxim],list[i]=list[i],list[maxim]
    return list

T=list(map(int,input().split()))
T=select_sort(T)
print(T)
