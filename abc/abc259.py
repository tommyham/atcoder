def proba():
    N,M,X,T,D=map(int, input().split())
    
    if M<=X:
        print(T-D*(X-M))
    else:
        print(T)

def probB():
    import math
    a,b,d=map(int, input().split())
    r=math.sqrt(a**2+b**2)
    if a:
        theta=math.degrees(math.atan2(b,a))
    else:
        if b>0:
            theta=90
        else:
            theta=-90
    theta+=d
    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians(theta))
    print(x,y)

# S=str(input())
# T=str(input())
S="abbaac"
T="abbbbaaac"
# S="xyzz"
# T="xyyzz"
s_count=0
t_count=0
s_start=0
t_start=0
judge=True
for i in range(s_start,len(S)):
    if S[s_start]==S[i]:
        s_count+=1
        continue
    
    for j in range(t_start,len(T)):
        if T[t_start]==T[j]:
            t_count+=1
            continue
        else:
            break
    s_start=i
    t_start=j
    if S[s_start]==T[t_start] and ((s_count<t_count and s_count>1) or s_count==t_count):
        s_count=1
        t_count=0
    else:
        judge=False
        break

if judge:
    print("Yes")
else:
    print("No")