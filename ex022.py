fullName = str(input("What`s your name? ")).strip()

fullNameUpper = fullName.upper()
fullNameLower = fullName.lower()
lenghtName = len(fullName) - fullName.count(' ')
lenghtOfFirst = len(fullName.split()[0])

print("""Your name is {}
Your name in capital letters is: {}
Your name in lowercase is: {}
Quantity of letters is: {}
Your first name have a: {} letters""".format(fullName, fullNameUpper, fullNameLower, lenghtName, lenghtOfFirst))