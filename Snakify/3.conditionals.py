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
    
#equal numbers
a = int(input())
b = int(input())
c = int(input())
d = 0
if a==b or a==c or c==b:
    d = d+2
if a==b and b==c and c==a:
    d = 3
print(d)

#rook move
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c or b==d:
    print("YES")
else:
    print("NO")
    
#same color
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
    
#king move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')

#bishop move
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (abs(a-c)) == (abs(b-d)):
    print("YES")
else:
    print("NO")
    
#queen move
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((abs(a-c)) == (abs(b-d))) or (a==c or b==d):
    print("YES")
else:
    print("NO")
    
#knight move
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((abs(a-c) == 1 and abs(b-d) == 2) or (abs(a-c) == 2) and abs(b-d) ==1):
    print("YES")
else:
    print("NO")
    
#chocolate bar
a = int(input())
b = int(input())
c = int(input())

if a*b > c and ((c%a == 0) or (c%b == 0)):
    print("YES")
else:
    print("NO")
    
#leap year
a = int(input())

if a%4 == 0 and a%100 != 0 or a%400 == 0:
    print("LEAP")
else:
    print("COMMON")