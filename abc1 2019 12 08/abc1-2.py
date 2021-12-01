s=0
s=list(input("Please input a word:"))
length=len(s)
print(length)
half=int(length/2)
print(half)
count=0
hug=0
while(count<half):
    if(s[count]!=s[length-count-1]):
        hug+=1
    else:
        pass
    count+=1
print("The number of hug is",hug,".")
