s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        vowels += 1

    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        consonants += 1

    elif '0' <= ch <= '9':
        digits += 1

    elif ch == ' ':
        spaces += 1

    else:
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)