def search(N,digit):
        divide=1
    for i in range(1,digit-2):
        divide+=10**i
    MOD=10**9+7
    count=0
    for i in range(1,9):
        for j in range(1,9):
            if(i!=j):
                if(i<int(SN[0])):
                    count+=divide+10**(digit-2)
                elif(i==int(SN[0]) and j<=int(SN[digit-1])):
                    count+=divide+int(SN[1:digit-2])
                elif(i==int(SN[0]) and j>int(SN[digit-1])):
                    count+=divide+int(SN[1:digit-2])-1
                else:
                    count+=divide
            else:
                if(i<int(SN[0])):
                    count+=divide+10**(digit-2)+1
                elif(i==int(SN[0]) and j<=int(SN[digit-1])):
                    count+=divide+int(SN[1:digit-2])
                elif(i==int(SN[0]) and j>int(SN[digit-1])):
                    count+=divide+int(SN[1:digit-2])-1
                else:
                    count+=divide
    return count

N=int(input())
SN=str(N)
digit=len(SN)
MOD=10**9+7
count=0
if(digit>2):
    count=search(N,digit)
else:

print(count)