#problem 1
print("please enter your name")
a = input()
print("1.rectangular/square 2.circular")
shape = int(input())
if shape == 1:
    print("please enter length")
    length = int(input())
print("please enter width")
width = int(input())
print("please enter height")
height = int(input())
area = (3.14*(width/2))**2
print(a)
if shape == 1:
    print("the rectangular/square pool will take", length*width*height*7.5, "gallons")
else:
    print((area*height*5.875))