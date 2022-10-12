def probA():
    L1,R1,L2,R2=map(int, input().split())
    length=0
    if L1<L2:
        if R1<=R2:
            length=R1-L2
        else:
            length=R2-L2
    else:
        if R2<=R1:
            length=R2-L1
        else:
            length=R1-L1
    
    if length<0:
        print(0)
    else:
        print(length)

def probB():
    N=int(input())
    A=[str(input()) for _ in range(N)]
    judge=True
    for i in range(N):
        for j in range(i+1,N):
            diff=abs(ord(A[i][j])-ord(A[j][i]))
            if (diff==0 and A[i][j]=="D") or diff==11:
                pass
            else:
                judge=False
                break
        if judge:
            pass
        else:
            break
    
    if judge:
        print("correct")
    else:
        print("incorrect")

# def probC():
N=int(input())
S=[str(input()) for _ in range(N)]
N=5
S=['newfile','newfile', 'newfile','newfile', 'newfile']

strings=set(S)
counts=[0 for _ in range(len(strings))]
 
for i in range(N):
    index=list(strings).index(S[i])
    
    if counts[index]:
        print(S[i]+"("+str(counts[index])+")")
    else:
        print(S[i])
        
    counts[index]+=1
        

# counts=[]
# strings=set()

# def checkString(s):
#     if s[0] in strings:
#         index=list(strings).index(s[0])
#         s[1]=index
#         counts[index]+=1
#     else:
#         strings.add(s[0])
#         counts.append(0)
        
#     if s[1]!=-1:
#         print(s[0]+"("+str(counts[index])+")")
#     else:
#         print(s[0])
    
#     return s[1]

# ans=list(map(checkString,S))

# N,M=map(int, input().split())
# X=list(map(int, input().split()))
# query=[list(map(int, input().split())) for _ in range(M)].sort()
# bornus=[[0,0] for _ in range(N)]
