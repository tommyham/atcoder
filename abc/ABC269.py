def probA():
    a,b,c,d=map(int, input().split())
    
    print((a+b)*(c-d))
    print('Takahashi')

def probB():
    S=[str(input()) for _ in range(10)]
    
    count=0
    for i in range(len(S)):
        s=S[i]
        if '#' in s:
            if count:
                pass
            else:
                A=i+1
                C=s.index('#')+1
                D=C+s.count('#')-1
                count+=1
        else:
            if count:
                B=i
                break
        
        if i==len(S)-1:
            B=len(S)
    
    print(A,B)
    print(C,D)

def probC():
    N=int(input())
    n=format(N,'b')
    index=[]
    
    while n.find('1')!=-1:
        index.append(n.find('1'))
        n=n.replace('1', '0',1)
    
    start='0'*len(index)
    if len(index):
        while len(start)<=len(index):
            copy_n=list(n)
            for i in range(len(start)):
                copy_n[index[i]]=start[i]
            print(int(''.join(copy_n),2))
            start=format(int(start,2)+1,'b').zfill(len(index))
    else:
        print(0)

N=int(input())
black=[list(map(int, input().split())) for _ in range(N)]
