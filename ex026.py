phrase = str(input("Write a phrase, please: ")).upper().strip()

countLetterA = phrase.count('A')
positionLetterA = phrase.find('A') + 1
finalLetterA = phrase.rfind('A') + 1

print("""In your phrase, have {} letters A
Your first appearance is in {}
And your last appearance is in {}""".format(countLetterA, positionLetterA, finalLetterA))