N=list(map(int,input().split()))
W=list(map(int,input().split()))
T=str(input())
n=N[0]
k=N[1]
a=n%k
b=n//k
count=0
w=[0]*k
for i in range(k):
    for  j in range(b):
        if(j==0):
            #print('{0} {1}'.format(T[i],w[i]))
            if(T[i]=='r'):
                  count+=W[2]
            elif(T[i]=='s'):
                  count+=W[0]
            else:
                  count+=W[1]
            w[i]=1
            #print(count)
        else:
            #print('{0} {1}'.format(T[i+(j-1)*k],T[i+j*k]))
            #print(w[i])
            if(T[i+(j-1)*k]==T[i+j*k] and w[i]==1):
                w[i]=0
            else:
                if(T[i+j*k]=='r'):
                    count+=W[2]
                elif(T[i+j*k]=='s'):
                    count+=W[0]
                else:
                    count+=W[1]
                w[i]=1
            #print(count)
for j in range(a):
    i=j+b*k
    l=j+(b-1)*k
    #print(T[i])
    #print(w[j])
    if(T[i]==T[l] and w[j]==1):
        count+=0
        w[j]=0
    else:
        if(T[i]=='r'):
            count+=W[2]
        elif(T[i]=='s'):
            count+=W[0]
        else:
            count+=W[1]
        w[j]=1
    #print(count)
print(count)
