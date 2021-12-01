
mov_vec=[[1,0],[0,1]]
def move_to(x,y,h):
    h[y][x]=1

def undo(x,y,h):
    h[y][x]=0

def search(A,B,N,x,y,s,t,h):
    global mov_vec
    t=0
    for dx,dy in mov_vec:
        x1=x+dx
        y1=y+dy
        print(x1,y1)
        if 0<=x1<N[1] and 0<=y1<N[0] and h[y1][x1]==0:
            move_to(x1,y1,h)
            print(h)
            s=abs(x-abs(A[y1][x1]-B[y1][x1]))
            if x1<N[1]-1 or y1<N[0]-1:
                t=search(A,B,N,x,y,s,t,h)
                print(t)
            else:
                pass
        else:
            pass
        if x1==N[1] and y1==N[0]:
            if s>t:
                s=t
                print(s)
            else:
                pass
        else:
            pass
    undo(x1,y1,h)
    print(h)
    return s

N=list(map(int,input().split()))
h=[[0 for i in range(N[1])] for j in range(N[0])]
print(h)
A=[]
B=[]
for i in range(N[0]):
    A.append(list(map(int,input().split())))
for i in range(N[0]):
    B.append(list(map(int,input().split())))
s=abs(A[0][0]-B[0][0])
t=0
x=0
y=0
h[0][0]=1
print(h)
s=search(A,B,N,x,y,s,t,h)
print(s)
print(A)
print(B)