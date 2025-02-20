nameFull = str(input("What`s your full name? ")).strip()

name = nameFull.split()

lastName = name[len(name) - 1]
print("""Your name: {}
First Name: {}
Last Name: {}""".format(nameFull,name[0], lastName))