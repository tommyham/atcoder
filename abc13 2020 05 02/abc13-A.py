K=int(input())
A,B=map(int,input().split())
a=A%K
b=B%K
ans=0
ans=a*b
if(ans==0):
    print("OK")
else:
    if((A+K-a)<=B or (B-b)>=A):
        print("OK")
    else:
        print("NG")