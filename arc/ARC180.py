import math
def main():
    N=int(input())
    S=input()

    number=int(1e9+7)

    patarn_numnbers=[]
    count=1
    pre=S[0]
    for i in range(1,N):
        if pre!=S[i]:
            count+=1
        else:
            num=math.floor((count+1)/2)
            if num!=0:
                patarn_numnbers.append(num)
            count=1
        pre=S[i]
    num=math.floor((count+1)/2)
    if num!=0:
        patarn_numnbers.append(num)
    
    ans=1
    for n in patarn_numnbers:
        ans=ans*n
    print(ans%number)

if __name__ == "__main__":
    main()