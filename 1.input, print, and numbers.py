#three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#hi john
a = input()
print('Hi ' + a)

#square
a = int(input())
print(a**2)

#right-angle triangle
b = int(input())
h = int(input())
print((b*h)/2)

# Hello, Harry
name = input()
print("Hello, " + name + "!")

#apple sharing
n = int(input())
k = int(input())
print(k // n)
print(k % n)

#previous and next
a = int(input())
b = a+1
c = a-1
d = str(a)
e = str(b)
f = str(c)
print("The next number for the number " + d + " is " + e + ".")
print("The previous number for the number " + d + " is " + f + ".")

#timestamps
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
time1 = (a*60*60)+(b*60)+(c)
time2 = (d*60*60)+(e*60)+(f)
time3 = time2 - time1
print(time3)

#desks
a = int(input())
b = int(input())
c = int(input())
class1 = (a//2)+(a%2)
class2 = (b//2)+(b%2)
class3 = (c//2)+(c%2)
desks = class1 + class2 + class3
print(desks)