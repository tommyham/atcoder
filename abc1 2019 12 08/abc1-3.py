N = int(input("Please input a anumber of people:"))
A = {}
for i in range(N):
    a = int(input("Please input a number of terethmony:"))
    l = []
    for j in range(a):
        tmp = list(map(int, input("Please input a terethmony:").split()))
        l.append(tmp[:])
        print(list(l))
    A[i+1] = l[:]
print(A)
 
ans = -1
for bit in range(2**N):
    l = []
    # 正直者と嘘つきの配列
    for i in range(N):
        if (bit >> i) & 1 == 1:
            l.append(1)
        else:
            l.append(0)
        print(list(l))    
    flag = True
    for i in range(N):
        if (bit >> i) & 1 == 1:
            for j in range(len(A[i+1])):
                if l[A[i+1][j][0]-1] != A[i+1][j][1]:
                    flag = False
    print(*l)
    print(flag)
    if flag:
        ans = max(ans, sum(l))
    # if len(l) <= 2:
    #     ans = 1
print(ans)
