def probA():
    Y=int(input())
    if not Y%400:
        print(366)
    elif not Y%100:
        print(365)
    elif not Y%4:
        print(366)
    else:
        print(365)

def probB():
    N=int(input())
    A=list(map(int,input().split()))
    index=list(range(N))

    A,index=zip(*sorted(zip(A,index)))
    print(index[-2]+1)

def probC():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort() # 低い順に並べる
    
    x=0
    S=sum(A) # 請求額の合計の算出
    # 合計より予算が大きければ無限に設定可能
    if S<=M:
        print("infinite")
        return True
    print(A)
    for a in A:
        print(a,x,N,M)
        # 残りの金額から支給額の上限に設定できるか検証
        if a*N<=M:
            x=a # 支給額の最大値xに設定
            N=N-1
            M=M-a
        else:
            # できない場合は，残りの支給対象に残額を均等に分配
            x=M//N
            break
    
    print(x)

    return False

def main():
    N=int(input())
    S=input()
    win={"R":"P","S":"R","P":"S"}

    win_S=""
    for s in S:
        win_S=win_S+win[s]

    count=0
    index=0
    continuous=False
    
    def check_replace_posibility(start,end,win_S):
        new_S=S[start].join(list(win_S[start:end+1]))
        
        win_S=win_S[:start]+new_S[:end-start+1]+win_S[end+1:]

        return win_S
    
    print(win_S)
    for i in range(len(win_S)-1):
        if win_S[i]==win_S[i+1] and not continuous:
            index=i
            continuous=True
        elif win_S[i]!=win_S[i+1] and continuous:
            win_S=check_replace_posibility(index,i,win_S)
            print(win_S)
            continuous=False
    if continuous:
        win_S=check_replace_posibility(index,len(win_S),win_S)
        print(win_S)

    print(count)

if __name__ == "__main__":
    # main()
    probC()