def probA():
    N,K,X=map(int,input().split())
    A=list(map(int,input().split()))
    print(*(A[:K]+[X]+A[K:]))

def probB():
    a ,b ,c ,d ,e ,f=map(int,input().split())
    g ,h ,i ,j ,k ,l=map(int,input().split())

    share=[]
    def check(p1,p2,q1,q2):
        start=p1
        end=q2
        if q1>=p2 or q2<=p1:
            return 0

        if p1<=q1:
            start=q1
        
        if q2<=p2:
            end=q2

        return end-start
    
    share.append(check(a,d,g,j))
    share.append(check(b,e,h,k))
    share.append(check(c,f,i,l))
    ans=1
    for s in share:
        ans*=s

    if ans==0:
        print("No")
    else:
        print("Yes")

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    
    ans=abs(A[N-K-1]-A[0])
    for i in range(1,len(A)-(N-K)+1):
        tmp=abs(A[i+(N-K)-1]-A[i])
        if ans>tmp:
            ans=tmp
    print(ans)
    
if __name__ =="__main__":
    main()