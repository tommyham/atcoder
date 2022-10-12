def probA():
    S=input()
    sum_all=10*(0+9)/2
    for s in S:
        sum_all-=int(s)
    print(int(sum_all))

def probB():
    A,B,K=map(int, input().split())
    count=0
    while A<B:
        A=A*K
        count+=1
    print(count)

N,M,K=map(int, input().split())
count=0
add=0
# 再帰制限に引っかかった場合に外す
# import sys
# sys.setrecursionlimit(100000)
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]
div=998244353
ans = cmb(K,N)
print(ans%div)