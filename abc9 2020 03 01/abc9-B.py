A=[[0 for i in range(3)] for j in range(3)]
for i in range(3):
    A[i]=list(map(int,input().split()))
N=int(input())
b=[]
for i in range(N):
    b.append(input())
    for j in range(3):
        for k in range(3):
            if(A[j][k]==int(b[i])):
                A[j][k]=0
            else:
                pass
B=[[0 for i in range(3)] for j in range(3)]
C=[[0 for i in range(3)] for j in range(2)]
for i in range(3):
    for j in range(3):
        if(i==j and i!=2):
            C[0][j]=A[i][j]
            B[i][j]=A[i][j]
        elif(i==j and i==2):
            C[0][j]=A[i][j]
            C[1][j]=A[i][j]
            B[i][j]=A[i][j]
        elif((i==0 and j==2) or (i==2 and j==0)):
            C[1][i]=A[i][j]
            B[j][i]=A[i][j]
        else:
            B[j][i]=A[i][j]
count=0
for i in A:
    if(i==[0,0,0]):
        count+=1
    else:
        pass
for i in B:
    if(i==[0,0,0]):
        count+=1
    else:
        pass
for i in C:
    if(i==[0,0,0]):
        count+=1
    else:
        pass
if(count>0):
    print("Yes")
else:
    print("No")