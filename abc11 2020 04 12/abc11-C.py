def gcd(a,b):
    if(a%b==0):
        return b
    else:
        b=gcd(b,a%b)
    return b

K=int(input())
count=0
way=0
for i in range(1,K+1):
    for j in range(i,K+1):
        way=gcd(j,i)
        for k in range(j,K+1):
            way=gcd(k,way)
            if(i==j and j==k):
                count+=way
            elif((i==j and j!=k) or (i!=j and j==k) or (i==k and j!=k)):
                count+=way*3
            else:
                count+=way*6
print(count)