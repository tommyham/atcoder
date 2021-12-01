N=int(input())
N=str(N)
judge=0
for i in N:
    if(i=="7"):
        judge=1
    else:
        pass
if(judge==1):
    print("Yes")
else:
    print("No")