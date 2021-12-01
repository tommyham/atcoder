a,b,c=0,0,0
while((a or b or c)<1 or 13<(a or b or c)):
    print("Please input a integral number from 1 to 13")
    a=int(input("Please input a integral number A1:"))
    b=int(input("Please input a integral number A2:"))
    c=int(input("Please input a integral number A3:"))
ans=a+b+c
if(ans<=21):
    print("win")
else:
    print("bust")
