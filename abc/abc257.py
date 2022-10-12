def probA():
    alphabet=[chr(ord("A")+i) for i in range(26)]
    N,X=map(int,input().split())
    
    num=X//N
    
    if X%N:
        pass
    else:
        num-=1
    print(alphabet[num])
def probB():
    N,K,Q=map(int,input().split())
    A=list(map(int,input().split()))
    L=list(map(int, input().split()))
    
    for l in L:
        if A[l-1]==N:
            pass
        else:
            if l==K:
                A[l-1]+=1
                continue
            if A[l]==A[l-1]+1:
                pass
            else:
                A[l-1]+=1

    for a in A:
        print(a,end=" ")

# N=int(input())
# S=str(input())
# W=list(map(int, input().split()))

# N=5
# S='10101'
# W=[60, 45, 30, 40, 80]

# kid=[W[i] for i in range(N) if S[i]=="0"]
# kid.sort(reverse=True)
# adult=[W[i] for i in range(N) if S[i]=="1"]
# adult.sort()

# ligther=[a for a in adult if a<=kid[0]]
# heavier=[k for k in kid if k>=adult[0]]

# def judge(kid,adult):
#     lighter=0

# N=int(input())
# query=[list(map(int, input().split())) for _ in range(N)]

N=4
query=[[-10, 0, 1], [0, 0, 5], [10, 0, 1], [11, 0, 1]]

need_power=[]

for i in range(len(query)):
    power=[]
    q=query[:i]
    q[len(q):len(q)]=query[i+1:]
    for j in range(len(q)):
        power.append((abs(query[i][0]-q[j][0])+abs(query[i][1]-q[j][1]))/query[i][2])
    need_power.append(min(power))
        