from time import sleep

print('*' * 40)
print('{:=^40}'.format(' Waiting for the new year... '))
print('*' * 40)

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print("{:🎉^25}".format(' HAPPY NEW YEAR '))