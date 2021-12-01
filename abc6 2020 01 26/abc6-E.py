def quick_sort(C):
    stand=C[1][0]/C[0][0]
    over=[[] for i in range(2)]
    same=[[] for i in range(2)]
    under=[[] for i in range(2)]
    for i in range(len(C[0])):
        if(C[1][i]/C[0][i]>stand):
            over[0].append(C[0][i])
            over[1].append(C[1][i])
        elif(C[1][i]/C[0][i]<stand):
            under[0].append(C[0][i])
            under[1].append(C[1][i])
        else:
            same[0].append(C[0][i])
            same[1].append(C[1][i])
    if(len(over[0])>1):
        over=list(quick_sort(over))
    else:
        pass
    if(len(under[0])>1):
        under=list(quick_sort(under))
    else:
        pass

    return [over[0]+same[0]+under[0],over[1]+same[1]+under[1]]

H,N=map(int,input().split())
C=[[0 for i in range(N)] for j in range(2)]
for i in range(N):
    C[0][i],C[1][i]=map(int,input().split())
C=quick_sort(C)
print(C)
count=0
while(H!=0):
    if(H%C[0][N-1]==0):
        print(H//C[0][N-1])
        count+=(H//C[0][N-1])*C[1][N-1]
        H=H%C[0][N-1]
    else:
        count+=(H//C[0][N-1])*C[1][N-1]
        print(H//C[0][N-1])
        H=H%C[0][N-1]
        for i in range(N):
            if(C[0][i]>=H):
                C[0][i]=H
            else:
                pass
        C=quick_sort(C)
        print(C)
print(count)