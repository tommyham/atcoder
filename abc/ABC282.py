def probA():
    K=int(input())
    start='A'
    ans='A'
    for i in range(1,K):
        ans+=chr(ord(start)+i)
    print(ans)

def probB():
    N,M=map(int,input().split())
    S=[str(input()) for _ in range(N)]
    ans=0
    
    def mutch(pair1,pair2):
        for p1,p2 in zip(pair1,pair2):
            if 'o' in [p1,p2]:
                pass
            else:
                return False
        return True
    
    for i in range(len(S)):
        pair1=S[i]
        for j in range(i+1,len(S)):
            pair2=S[j]
            if mutch(pair1,pair2):
                ans+=1
    print(ans)

def probC():
    N=int(input())
    S=str(input())
    
    split_S=S.split('"')
    judge=True
    
    for i in range(len(split_S)):
        if judge:
            split_S[i]=split_S[i].replace(',', '.')
        judge= not judge
    print('"'.join(split_S))

def probD():
    N,M=map(int, input().split())
    query=[list(map(int, input().split())) for _ in range(M)]

def main():
    N,M=map(int, input().split())
    A=list(map(int,input().split()))

if __name__ in '__main__':
    main()