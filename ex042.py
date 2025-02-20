firstMeasure = float(input("Enter a first measure: "))
secMeasure = float(input("Now, the second measure: "))
lastMeasure = float(input("Finally, the last measure: "))

if firstMeasure < secMeasure + lastMeasure and secMeasure < firstMeasure + lastMeasure and lastMeasure < secMeasure + firstMeasure:
    if firstMeasure == secMeasure == lastMeasure:
        print("It`s possible build a equilateral triangle!")
    elif firstMeasure == secMeasure or secMeasure == lastMeasure or firstMeasure == lastMeasure:
        print("It`s possible build a isosceles triangle!")
    elif firstMeasure != secMeasure and secMeasure != lastMeasure and firstMeasure != lastMeasure:
        print("It`s possible build a scalene triangle!")
else:
    print("Isn`t possible build a triangle!")