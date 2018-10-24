#last digit of int
a = int(input())
print(a%10)

#tens digit
a = int(input())
print(a//10%10)

#sum of digits
a = int(input())
b = a%10
c = a//10%10
d = a//100
print(b+c+d)

#fractional part
a = float(input())
print(a%1)

#first digit past decimal
a = float(input())
print(int(a%1//.1))

#car route
from math import ceil
a = int(input())
b = int(input())
print(ceil(b/a))

#digital clock
a = int(input())
b = str(a//60)
c = str(a%60)
print(b, c)

#total cost
a = int(input())
b = int(input())
n = int(input())
print(a*n+b*n//100, b*n%100)

#clock face 1
h = int(input())
m = int(input())
s = int(input())
print((h*3600+m*60+s)/120)

#clock face 2
a = float(input())
print(a%30*12)