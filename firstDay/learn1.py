log=open('a.txt','a')
print('a','b','c',file=log)
print('e','f','g')
a=5 if 1 > 3 else 0
print(a)
a=2 and 3
b=2 or 3
print(a,b)

x=99
z=10
def addData(y):
    z=x+y
    return z
def addData2(y):
    x=100
    z=x+y
    return z
def addData3(y):
    global z
    z=50
    return y+z

print(addData(100))
print(addData2(100))
print(addData3(100))
print(z)

def proYield(n):
    for i in range(n):
        print(i,'start')
        yield i ** 2
        print(i,'stop')

for i in proYield(5):
    print(i)


import sys
print(sys.path)
import firstDay.learn2
print(firstDay.learn2.lp)
import learn2
print(learn2.lp)