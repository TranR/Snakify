#series1
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i)
    
#series2
a = int(input())
b = int(input())

if b > a:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
        
#sum of 10
res = 0
for i in range(10):
    res += int(input())
print(res)

#sum of n
a = int(input())
res = 0
for i in range(1, a+1):
    res += int(input())
print(res)

#sum of cubes
a = int(input())
num = 0
for i in range(a+1):
    num += i**3
print(num)

#factorial
a = int(input())
n = 1
for i in range(1, a+1):
    n = n*i
print(n)

#num zero
a = int(input())
res = 0
for i in range(1, a+1):
    if int(input()) == 0:
        res = res+1
print(res)

#adding factorials
a = int(input())
n = 1
u = 0
for i in range(1, a+1):
    n = n*i
    u += n
print(u)

#ladder
a = int(input())
b = ""
for i in range(1,a+1):
    b = b+str(i)
    print(b)
    
#lost card
a = int(input())
b = 0
c = 0
for i in range(1, a+1):
    b += i
for i in range(1, a):
    c += int(input())
b -= c
print(b)