s=input("Enter a string:")
rev=""
for i in s:
    rev=i+rev

    if s == rev:
        print("palindrome")
    else:
        print("not a palindrome")