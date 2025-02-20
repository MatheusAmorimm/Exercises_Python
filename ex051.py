firstTerm = int(input('insert a first term of the PA: '))
ratio = int(input('What is the ration for arithmetic progession? '))

for c in range(10):
    terms = firstTerm + c * ratio
    print(terms)
