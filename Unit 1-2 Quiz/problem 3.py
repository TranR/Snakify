print("please enter the number")
a = int(input())
if a%10*10 == 0:
    print("0" + str(a//10))
else:
    print((a//10) + (a%10*10))