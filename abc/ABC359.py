def probA():
    N=int(input())
    count=0
    for _ in range(N):
        s=input()
        if s=="Takahashi":
            count+=1
    print(count)

def probB():
    N=int(input())
    A=list(map(int,input().split()))

    count=0
    for i in range(len(A)-2):
        if A[i]==A[i+2]:
            count+=1
    print(count)

def main():
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))

    # 初期座標のタイルが左右どちらかの判定
    left=False
    if S[1]>=0:
        if (S[0]%2==0 and S[1]%2==0) or (S[0]%2==1 and S[1]%2==1):
            left=True
    else:
        if (S[0]%2==0 and S[1]%2==1) or (S[0]%2==1 and S[1]%2==0):
            left=True
    
    # 横移動方向とタイルの位置が異なる場合，一致させる処理
    if S[0]>T[0] and not left:
        S[0]-=1
        left=True
    elif S[0]<T[0] and left:
        S[0]+=1
        left=False
    
    # 移動金額の計算 ※初期座標のタイルの左右と横移動の向き（左右）が一致した場合のみ
    ans=abs(S[1]-T[1])
    if ans >= abs(S[0]-T[0]): # 上方向の移動量＞＝左右の移動量
        pass
    else: # 上方向の移動量＜左右の移動量
        ans+=(abs(S[0]-T[0])-ans+1)//2
    print(ans)

if __name__ == "__main__":
    main()