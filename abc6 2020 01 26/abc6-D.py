H=int(input())
count=0
while(H!=1 and H!=0):
    H=H//2
    count+=1
print(2**(count+1)-2+1)