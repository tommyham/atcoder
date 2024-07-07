def probA():
    S,T=map(str,input().split())

    if S=="AtCoder" and T=="Land":
         print("Yes")
    else:
         print("No")

def probB():
     N,A=map(int,input().split())
     T=list(map(int,input().split()))

     time=T[0]+A
     print(time)
     for i in range(1,len(T)):
        if T[i]<=time:
            time+=A
            print(time)
        else:
            time=T[i]+A
            print(time)

def probC():
    N,M=map(int,input().split())
    S=[]
    for _ in range(N):
        S.append("0b"+input().replace("x","0").replace("o","1"))
    
    ans=N
    for i in range(1,2**(N)):
        bit_number=format(i,"0"+str(N)+"b")
        bit_shop=format(0,"#0"+str(N)+"b")
        temp_ans=0
        for j in reversed(range(len(bit_number))):
            if bit_number[j]=="1":
                bit_shop=bin(int(bit_shop,2)|int(S[j],2))
                temp_ans+=1
        if bit_shop.count("1")==M:
            if ans>temp_ans:
                ans=temp_ans
    print(ans)

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    
    payment=0
    distribute=False
    while len(B)>=1:
        max_sub_payment=1e9
        max_index=-1
        for i in range(len(A)):
            sub_payment=A[i]-B[0]
            if sub_payment==0:
                payment+=A.pop(i)
                B.pop(0)
                break
            elif sub_payment>0:
                if max_sub_payment>sub_payment:
                    max_index=i
                    max_sub_payment=sub_payment
            else:
                pass

            if i==len(A)-1:
                payment+=A.pop(max_index)
                B.pop(0)
        if len(B)==0:
            distribute=True
            break
        if max_index==-1 or len(A)==0:
            break
    if distribute:
        print(payment)
    else:
        print(-1)

if __name__ == "__main__":
    main()