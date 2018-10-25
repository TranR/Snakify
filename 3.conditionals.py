#min of two
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)

#sign function
a = int(input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)
    
#min of 3
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)