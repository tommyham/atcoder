import math
X=int(input())
origin=100
count=0
while(origin<X):
    origin+=int(origin*0.01)
    count+=1
print(count)