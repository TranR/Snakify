print("please enter the day of the year")
k = (int(input())+3)
if k%7 == 0:
    print("sunday")
elif k%7 == 1:
    print("monday")
elif k%7 == 2:
    print("tuesday")
elif k%7 == 3:
    print("wednesday")
elif k%7 == 4:
    print("thursday")
elif k%7 == 5:
    print("friday")
elif k%7 == 6:
    print("saturday")