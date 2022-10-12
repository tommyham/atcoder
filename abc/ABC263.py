def probA():
    num=list(map(int, input().split()))
    num1=[n for n in num if n==num[0]]
    num2=[n for n in num if n!=num[0]]
    
    if len(num1)==3 and num2.count(num2[0])==2:
        print("Yes")
    elif len(num1)==2 and num2.count(num2[0])==3:
        print("Yes")
    else:
        print("No")

def probB():
    N=int(input())
    P=list(map(int, input().split()))
    
    ans=0
    pepole=N
    while pepole!=1:
        pepole=P[pepole-2]
        ans+=1
    print(ans)

def probC():
    N,M=map(int, input().split())
    
    def searchDictNum(n,start=1,S=[]):
        for i in range(start,M+1):
            S.append(i)
            if n!=1:
                searchDictNum(n-1,i+1,S)
            else:
                print(*S)
            S.pop(-1)
    
    searchDictNum(N)

def probD():
    N,L,R=map(int, input().split())
    A=list(map(int, input().split()))
    ans=sum(A)
    S=sum(A)
    
    Sdl=0
    Dl=0
    Sdr=R*(N)-S
    
    ans=min(ans,sum(A)+Sdr) # すべてRに置き換える場合を最初に比較
    # RとLの置き換えを同時に進行
    # Lから先に置き換えるとLの途中までRで置き換えた方が最小になる場合を考慮できない
    # 全探索を始めに考え、そこから改良していくのがコード的には正しい※計算式を立てられるならなおよい
    for i in range(N):
        # 左端から順にLに変えた際の差分を計算
        Sdl+=L-A[i]
        # Aのiより小さい要素のいくつかを置き換えた際の最小と比較
        Dl=min(Dl,Sdl)
        # iより前をすべてRで置き換えた場合の差分を計算
        Sdr+=A[i]-R
        
        ans=min(ans,S+Sdr+Dl)
    
    print(ans)