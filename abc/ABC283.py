def probA():
    A,B=map(int, input().split())
    print(A**B)

def probB():
    N=int(input())
    A=list(map(int, input().split()))
    Q=int(input())
    query=[list(map(int, input().split())) for _ in range(Q)]
    
    for q in query:
        if q[0]==1:
            A[q[1]-1]=q[2]
        elif q[0]==2:
            print(A[q[1]-1])

def probC():
    S=str(input())
    S=S.split('00')
    ans=len(S)-1
    
    for s in S:
        ans+=len(s)
    
    print(ans)

def probD():
    S=str(input())
    S=S.split(')')
    
    for s in S:
        s=s.replace('(','')
        if len(s)==len(set(s)):
            continue
        else:
            print('No')
            return False
    print('Yes')
    
    return True

# 孤立した要素があるかを確認する関数(O(4*H*W))
def checkDepend(A):
    for i,a_l in enumerate(A):
        for j,a in enumerate(a_l):
            try:
                if a==A[i][j+1]:
                    continue
            except:
                pass
            
            try:
                if a==A[i+1][j]:
                    continue
            except:
                pass
            
            if i!=0:
                if a==A[i-1][j]:
                    continue
            
            if j!=0:
                if a==A[i][j-1]:
                    continue
            
            return False
    
    return True

def reversal(A,i=0,count=0):
    if checkDepend(A):
        print(i,count,'success')
        return True,count
    
    if i==len(A):
        print(i,count,'over')
        return False,-1
        
    judge,ans=reversal(A,i+1)
    if judge:
        print(i,count,'unreversal')
        return True,ans
    
    A[i]=[(not a)*1 for a in A[i]]
    judge,ans=reversal(A,i+1,count+1)
    if judge:
        print(i,count,'reversal')
        return True,ans
    print(i,count,'false')
    return False,-1

def main():
    H,W=map(int, input().split())
    A=[list(map(int, input().split())) for _ in range(H)]
    print(reversal(A))
    
if __name__ == '__main__':
    main()