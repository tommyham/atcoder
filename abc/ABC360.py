def probA():
    S=input()

    for s in S:
        if s=="M":
            print("No")
            return False
        elif s=="R":
            print("Yes")
            return True

def probB():
    S,T=input().split()

    def split_string(w,c):
        split_T=""
        for i in range(0,len(S),w):
            if len(S[i:i+w])<c:
                break
            split_T+=S[i:i+w][c-1]
        return split_T

    for w in range(1,len(S)):
        for c in range(1,w+1):
            split_T=split_string(w,c)
            if split_T==T:
                print("Yes")
                return True
    print("No")
    return False

def main():
    N=int(input())
    A=list(map(int,input().split()))
    W=list(map(int,input().split()))

    exist={i:0 for i in range(N)}
    cost=0
    for i in range(N):
        weight=exist[A[i]-1]
        if weight==0:
            exist[A[i]-1]=W[i]
        else:
            if weight>W[i]:
                cost+=weight
                exist[A[i]-1]=W[i]
            else:
                cost+=W[i]
    print(cost)

if __name__ == "__main__":
    main()