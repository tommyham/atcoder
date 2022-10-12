def probA():    
    a,b,c=map(int, input().split())
    
    if (a-b>=0 and b-c>=0) or (a-b<=0 and b-c<=0):
        print("Yes")
    else:
        print("No")

def probB():
    H,W=map(int, input().split())
    S=[input() for _ in range(H)]
    
    index=[]
    for i,s in enumerate(S):
        if "o" in s:
            temp=[j for j,x in enumerate(s) if x=="o"]
            index+=[[i,j] for j in temp]
        if len(index)==2:
            break
    
    diff=[abs(i-j) for i,j in zip(index[0],index[1])]
    print(sum(diff))

S=[]
maxim=0
minim=0
# Q=int(input())
# query=[list(map(int, input().split())) for _ in range(Q)]

Q=8
query=[[1, 3], [1, 2], [3], [1, 2], [1, 7], [3], [2, 2, 3], [3]]
def func(q):
    if q[0]==1:
        S.append(q[1])
    elif q[0]==2:
        num=min(q[2],S.count(q[1]))
        [S.remove(q[1]) for _ in range(num)]
    else:
        print(max(S)-min(S))

list(map(func, query))