string = input("Enter a string: ")
result = ""
for char in string:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char

print(result)