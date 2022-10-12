# T=int(input())
# num=[]
# S=[]
# for _ in range(T):
#     num.append(list(map(int, input().split())))
#     S.append(str(input()))

T=4
num=[[3, 2], [4, 2], [6, 3], [10, 5]]
S=['1??', '?1?0', '011?1?', '00?1???10?']

for n,s in zip(num,S):
    ones=s.count('1')
    zeros=s.count('0')
    questions=s.count('?')
    
    # 1の数と？の数を足しても規定値に達していなかったら次の要素へ
    if ones+questions<num[1]:
        print('No')
        continue
    
    