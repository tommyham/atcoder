def probA():
    N=int(input())
    age=10**9
    
    index=0
    S=[]
    for i in range(N):
        s,a=input().split()
        if int(a)<=age:
            index=i
            age=int(a)
        S.append(str(s))
    
    S=S[index:]+S[:index]
    
    for s in S:
        print(s)

def probB():
    N=int(input())

    if N<=10**3-1:
        print(N)
    elif N<=10**4-1:
        print(str(N)[:-1]+str(0))
    elif N<=10**5-1:
        print(str(N)[:-2]+str(0)*2)
    elif N<=10**6-1:
        print(str(N)[:-3]+str(0)*3)
    elif N<=10**7-1:
        print(str(N)[:-4]+str(0)*4)
    elif N<=10**8-1:
        print(str(N)[:-5]+str(0)*5)
    elif N<=10**9-1:
        print(str(N)[:-6]+str(0)*6)

def main():
    N,D=map(int,input().split())
    inside=[[] for _ in range(N)]

    X,Y=[],[]
    for i in range(N):
        x,y=map(int,input().split())
        X.append(x)
        Y.append(y)

        for j in range(len(X[:-1])):
            d=((X[j]-x)**2+(Y[j]-y)**2)**(1/2)
            if d<=D:
                inside[i].append(j)
                inside[j].append(i)
                
    infection=[0 for _ in range(N)]
    infection[0]=1

    def check(infecter,pre_infecter):
        length=len(inside[infecter])
        for i in range(length):
            try:
                near=inside[infecter].pop(0)
                if near==pre_infecter:
                    continue
                infection[near]=1
                check(near,infecter)
            except:
                pass
    
    check(0,-1)
    for i in infection:
        if i:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()