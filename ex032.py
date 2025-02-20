#currentYear = int(input('What year were we? '))
leapYear = int(input("Which year do you want to know if it is a leap year? "))

#testCent_Ten = currentYear - leapYear

#if testCent_Ten <= 99:
    #testLeapYear = leapYear % 4
    #if testLeapYear == 0:
        #print("Yeah, is a leap year!")
#elif testCent_Ten > 100:
    #testLeapYear = leapYear % 400
    #if testLeapYear == 0:
        #print("Yeah, is a leap year")
#else:
#    print("No, isn`t a leap year!")

if leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0:
    print("Yeah, {} is leap year".format(leapYear))
else:
    print("No, isn't a leap year")