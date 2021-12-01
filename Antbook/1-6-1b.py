K,S=map(int,input().split())
count=0
for X in range(K+1):
    for Y in range(K+1):
        com=S-(X+Y)
        if(com>=0 and com<=K):
            count+=1
        else:
            pass
print(count)