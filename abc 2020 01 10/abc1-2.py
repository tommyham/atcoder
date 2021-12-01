N=int(input())
S=str(input())
count=0
print(S[N])
for i in range(N-2):
    if(S[i:i+3]=="ABC"):
        count+=1
    else:
        pass
print(count)
