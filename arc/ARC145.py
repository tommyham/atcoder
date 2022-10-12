N=int(input())
S=str(input())

judge=True
for i in range(N//2):
    if i==N//2-1:
        if not N%2:
            if S[i:i+2]=="BB" or S[i:i+2]=="AA":
                continue
            else:
                judge=False
                break
        else:
            if S[i:i+2]=="BB" or S[i:i+2]=="AB":
                continue
            elif S[N-i-2:N-i]=="AA" or S[N-i-2:N-i]=="BA":
                continue
            else:
                judge=False
                break
    
    if S[i:i+2]== S[::-1][i:i+2]:
        continue
    if S[i:i+2]=="BA":
        S=S[:N-i-2]+"AB"+S[N-i:]
    elif S[N-i-2:N-i]=="BA":
        S=S[:i]+"AB"+S[i+2:]
    else:
        judge=False
        break

if judge:
    print("Yes")
else:
    print("No")