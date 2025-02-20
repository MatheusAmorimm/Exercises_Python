firstMeasure = float(input("What`s the first measure? "))
secMeasure = float(input("Now, enter the second measure: "))
lastMeasure = float(input("The last measure is: "))

if firstMeasure < secMeasure + lastMeasure and secMeasure < firstMeasure + lastMeasure and lastMeasure < firstMeasure + secMeasure:
    print("Using your measures is possible build a triangle!")
else:
    print('Isn`t possible build a triangle!')