def probA():
    A,B=map(int,input().split())
    if A==B:
        print(1)
    elif abs(A-B)%2:
        print(2)
    else:
        print(3)

def probB():
    N=int(input())

    l=-1
    r=-1
    fatigue=0
    for _ in range(N):
        A,S=input().split()
        A=int(A)

        if S=="L":
            if l==-1:
                l=A
            else:
                fatigue+=abs(l-A)
                l=A
        elif S=="R":
            if r==-1:
                r=A
            else:
                fatigue+=abs(r-A)
                r=A
    print(fatigue)

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def probC():
    N=int(input())
    A=list(map(int,input().split()))

    if N==1:
        print(1)
        return False

    answer=0
    count=1
    pre_A=A[1]
    pre_diff =A[1]-A[0]
    for i in range(2,N):
        if A[i]-pre_A==pre_diff:
            count+=1
        else:
            answer+=cmb(count+1,2)
            count=1
        pre_diff=A[i]-pre_A
        pre_A=A[i]
    answer+=cmb(count+1,2)
    
    answer+=N
    print(answer)

def main():
    N=int(input())
    A=list(map(int,input().split()))

if __name__ == "__main__":
    main()