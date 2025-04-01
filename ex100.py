from random import randint
values = []

def rand():
    for i in range(0, 5):
        values.append(randint(0, 10))

def sumeven(lst):
    sums_even = 0
    for num in range(len(lst)):
        if lst[num] % 2 == 0:
            sums_even += lst[num]
    print(sums_even)

rand()
print(values)
sumeven(values)