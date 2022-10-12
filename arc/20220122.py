def probA():
    N=int(input())
    A=list(map(int,input().split()))
    prev=0
    x=0
    for a in A:
        now=a
        if prev<=a:
            x=a
            prev=a
        else:
            break
    ans=[a for a in A if a!=x]
    print(*ans,sep=' ')

def myIndex(l,x):
    if x in l:
        return l.index(x)
    else:
        return False

def diving(multiple,l=0,depth=0):
    for i in range(len(multiple)):
        ind=myIndex(multiple[i][l:], 1)
        if ind!=False:
            lay=depth+1
            diving(multiple[i+1:],ind+1,lay)
        else:
            
# N=int(input())
# P=list(map(int,input().split()))
# Q=list(map(int,input().split()))
N=10
P=[4, 3, 1, 10, 9, 2, 8, 6, 5, 7]
Q=[9, 6, 5, 4, 2, 3, 8, 10, 1, 7]
multiple=[]
for p in P:
    multiple.append([0 if q%p else 1 for q in Q])
ans=[]
for m in multiple:
    for i in range(len(ans)):
        ind=myIndex(m[ans[i][-1]+1:],1)
        print(m[ans[i][-1]:])
        if ind!=False:
            ans[i].append(ans[i][-1]+1+ind)
        else:
            pass
    ans.append([myIndex(m,1)])
    