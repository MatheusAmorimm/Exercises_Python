number = int(input("Enter a integer number: "))
userOption = int(input("""[ 1 ] convert to BINARIE
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL
Your choice: """))

if userOption == 1:
    print("{} converted to binarie is {}".format(number, bin(number)[2:]))
elif userOption == 2:
    print("{} converted to octal is {}".format(number, oct(number)[2:]))
elif userOption == 3:
    print("{} converted to hexadecimal is {}".format(number, hex(number)[2:]))
else:
    print("Invalid option, try again")