# T=int(input())
# case=[str(input()) for _ in range(T)]

T=3
case=['1412', '23', '498650499498649123']

def compare(num,repeat):
    for j,t in enumerate(zip(num,repeat)):
        t=list(t)
        diff=int(t[0])-int(t[1])
        if diff<0:
            t[1]=int(t[1])-1
            if t[1]:
                repeat=str(int(repeat)-int(repeat[j])*(len(repeat)-j)+t[1]*(len(repeat)-j))
                return repeat
            else:
                if j:
                    repeat=str(int(repeat)-int(repeat[j])*(len(repeat)-j)+t[1]*(len(repeat)-j))
                    return repeat
                else:
                    repeat=repeat[1:]
                    return repeat
    return repeat

for c in case:
    ans=0
    for n in range(1,len(c)//2+1):
        if len(c)%n:
            num="9"*(len(c)-1)
        else:    
            split = [c[idx:idx + n] for idx in range(0,len(c), n)]
            repeat=split[0]
            for i in range(1,len(split)):
                diff=int(split[i])-int(repeat)
                if diff>0:
                    num=repeat*len(split)
                    break
                elif diff==0:
                    num=repeat*len(split)
                    continue
                else:
                    repeat=compare(split[i], repeat)
                
                if len(repeat)-n<0:
                    num="9"*(len(c)-1)
                    break
                else:
                    num=repeat*len(split)

        if ans<int(num):
            ans=int(num)
    print(ans)