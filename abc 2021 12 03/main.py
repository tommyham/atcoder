def probA():
    N=input().split()
    N=int(N[0])
    if N>=42:
        print("AGC0"+str(N+1))
    elif N<10:
        print("AGC00"+str(N))
    else:
        print("AGC0"+str(N))

def probB():
    def search(S):
        T="oxx"*7
        lengthS=len(S)
        lengthT=len(T)
        for l in range(lengthT-lengthS):
            flag=0
            i=0
            r=l
            for r in range(l,l+lengthS):
                if S[i]==T[r]:
                    r+=1
                    i+=1
                else:
                    flag=1
                    break
            if flag==0:
                print("Yes")
                return True
        print("No")
        return False
    
    S=input().split()
    S=S[0]
    search(S)

N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
#Grid=[["."]*(Q-P+1) for i in range(S-R+1)]
#k1=max(1-A,1-B)-1
#k1=[A+k1,B+k1]
#k2=max(1-A,B-N)-1
#k2=[A+k2,B-k2]
Grid=[["."]*N for i in range(N)]
k1=[i for i in range(max(P-A,R-B),min(Q-A,S-B)+1)]
k2=[i for i in range(max(P-A,B-S),min(Q-A,B-R)+1)]
Axisk1=[[A+i-1,B+i-1] for i in k1]
Axisk2=[[A+i-1,B-i-1] for i in k2]
#for i in Axisk1:
#    Grid[i[0]][i[1]]="#"
#for i in Axisk2:
#    Grid[i[0]][i[1]]="#"
#for i in range(P-1,Q):
#    temp="".join(Grid[i][R-1:S])
#    print(temp)