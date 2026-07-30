s=input("enter a string:")
old=input("enter a character to be replaced:")
new=input("enter a new character:")
result=""
for i in s:
    if i==old:
        result=result+new
    else:
        result=result+i
        print("the new string is:",result)
        