# This file is the codes for Atcoder Beginners Selection.

def PracticeA():
    a=int(input())
    b,c=map(int, input().split())
    s=str(input())
    
    print(a+b+c,s)

def ABC086A():
    a,b=map(int, input().split())
    if a%2 and b%2:
        print('Odd')
    else:
        print('Even')

def ABC081A():
    S=int(input())
    ans=0
    for i in range(1,4):
        if S%(10**i):
            ans+=1
            S-=S%(10**i)
    print(ans)

def ABC081B():
    N=int(input())
    A=list(map(int, input().split()))
    ans=10**9
    for a in A:
        if a%2:
            ans=0
            break
        count=0
        while not a%2:
            a=a//2
            count+=1
        
        ans=min(count,ans)
    print(ans)

def ABC087B():
    num_coin=[int(input()) for _ in range(3)]
    X=int(input())
    ans=0
    
    for a in range(num_coin[0]+1):
        for b in range(num_coin[1]+1):
            for c in range(num_coin[2]+1):
                if X==a*500+b*100+c*50:
                    ans+=1
    print(ans)

def ABC083B():
    N,A,B=map(int, input().split())
    ans=0
    
    for n in range(1,N+1):
        string_n=str(n)
        digits_sum=0
        for i in range(len(string_n)):
            digits_sum+=int(string_n[i])
        if A<=digits_sum and digits_sum<=B:
            ans+=n
    print(ans)

def ABC088B():
    N=int(input())
    A=sorted(list(map(int, input().split())),reverse=True)
    
    All=sum(A)
    Alice=sum(A[::2])
    
    print(Alice-(All-Alice))

def ABC085B():
    N=int(input())
    D=set(int(input()) for _ in range(N))
    
    print(len(D))

def ABC085C():
    N,Y=map(int, input().split())
    max_count=Y//1000
    
    for x in range(0,max_count//10+1):
        for y in range(0,(max_count-10*x)//5+1):
            if max_count-9*x-4*y==N:
                print(x,y,N-x-y)
                return True
    print(-1,-1,-1)
    return False

def ABC049C():
    S=str(input())
    
    while len(S):
        if S[:11]=='dreameraser':
            S=S[11:]
        elif S[:10]=='dreamerase':
            S=S[10:]
        elif S[:7]=='dreamer':
            S=S[7:]
        elif S[:6]=='eraser':
            S=S[6:]
        elif S[:5] in ['dream','erase']:
            S=S[5:]
        else:
            print('NO')
            return False
    print('YES')
    return True

def ABC086C():
    N=int(input())
    query=[list(map(int, input().split())) for _ in range(N)]
    start=[0]*3
    
    for goal in query:
        dt=goal[0]-start[0]
        move=abs(goal[1]-start[1])+abs(goal[2]-start[2])
        if not move:
            if dt%2:
                print('No')
                return False
        elif not dt%move:
            start=goal
        else:
            print('No')
            return False
    print('Yes')
    return True

def main():
    N=int(input())

if __name__ in '__main__':
    main()