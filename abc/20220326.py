def probA():
    A,B,C,D=map(int, input().split())
    hour=A-C
    minute=B-D
    if hour<0:
        print("Takahashi")
    elif hour>0:
        print("Aoki")
    else:
        if minute<=0:
            print("Takahashi")
        else:
            print("Aoki")
def probB():
    N=int(input())
    A=list(map(int, input().split()))
    A=list(set(A))
    ans=0
    for a in A:
        if a==ans:
            ans+=1
        else:
            break
    print(ans)

# N,K=map(int, input().split())
# A=list(map(int, input().split()))
# B=list(map(int, input().split()))
N,K=5,4
A=[9, 8, 3, 7, 2]
B=[1, 6, 2, 9, 5]
# diff_AA=list(abs(A[i]-A[i+1])for i in range(N-1))
# diff_BB=list(abs(B[i]-B[i+1])for i in range(N-1))
# diff_AB=list(abs(A[:-1][i]-B[1:][i])for i in range(N-1))
# diff_BA=list(abs(B[:-1][i]-A[1:][i])for i in range(N-1))
# diff=[diff_AA,diff_AB,diff_BA,diff_BB]
# for i in range(diff):
#     for j in range(N):
#         if diff[i][j]<0:
def diff(a,b):
    if abs(a-b)<=K:
        return True
    else:
        return False

def left(a,i):
    return diff(a[i], a[i+1])

def right(a,b,i):
    return diff(a[i],b[i+1])

def judge(i,node=0):
    if i==N-1:
        return True
    if node==0:
        if left(A, i):
            return judge(i+1,0)
        elif right(A,B,i):
            return judge(i+1,1)
        else:
            return False
    elif node==1:
        if left(B, i):
            return judge(i+1,0)
        elif right(B, A, i):
            return judge(i+1,1)
        else:
            return False
ans=judge(0,0)
ans2=judge(0,1)