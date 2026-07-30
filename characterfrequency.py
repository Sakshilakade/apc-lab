s=input("enter a strng:")
ch=input("enter a character to search:")
count=0
for i in s:
    if i==ch:
        count+=1
        print("the frequency is:", count)