s='hello heworld'
len(s)
s.split(' ')
p=s.replace('he','we',1)
print(p)
l=[1,2,3]
l.sort(reverse=True)
print(l)
l.pop(1)
print(l)
l.extend([1,2,3])
print(l)
d={'name':'zs','age':20}
print(d.values())
print(d.keys())
d.pop('name')
print(d)
d={}
d=dict.fromkeys(['a','b','c'],1)
print(d)
e=dict(name='zs',age=40)
print(e)
import os
s=os.getcwd()
print(os.listdir(s))
f=open('a.txt','w')
f.writelines(['1234\n','5678'])
f.close()
with open('a.txt','r') as f:
    print(f.readlines())


a=5
b=10
if a > b:
    print('a大于b')
    if a > 0:
        print('a是一个正数')
else:
    print('a小于等于b')
a=10 if 5>6 else 30
print(a)
a=0
while a<5:
    a+=1
    if a>3:
        break
else:
    print('out')
a=range(0,10,2)
for i in a:
    print(i)
l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
l3=zip(l1,l2)
print(list(l3))
for (offer,item) in enumerate(range(5),1):
    print(offer,item)




def addData(a,b):
    count=10
    return 10+a+b

c=addData(10,20)
print(c)
f=addData
print(f(1,2))






X=99
def test():
    X=98
    return X+1
print(test())
print(X)

X=99
def test():
    global X
    X=98
    return X+1
print(test())
print(X)


def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter

def test1(a,b,c):
    return a+b+c
def test2(a,b=2,c=3):
    return a+b+c
def test3(*a):
    t=list(a)
    count=0
    for i in t:
        count+=i
    return count

def test4(**kwargs):
    print(dict(kwargs))

print('*******************************')
print(test1(1,2,3))
print(test1(b=2,c=3,a=1))
print(test2(2))
print(test2(2,3,4))
print(test2(2,3))
print(test3(1,2,3))
print(test4(name='zs',age=15))


f=lambda x:x+1
print(f(5))

f=lambda x,y,z:x+y+z
print(f(1,4,5))



key='one'
d={'one':lambda x:x+2,
   'two':lambda x:x*2,
   'three':lambda x:x**2}
print(d[key](2))
f=map(lambda x:x+10,[1,2,3,4])
print(list(f))
f=map(pow,[1,2,3],[2,3,4])
print(list(f))

print(list(filter(lambda x:x>0,[-1,-2,4,5,6])))
from functools import reduce
s=reduce(lambda x,y:x+y,[1,2,3,4],-1)
print(s)

L=[]
for x in [1,2,3]:
    for y in [100,200,300]:
        L.append(x+y)


print(L)



L=[x+y for x in [1,2,3] for y in [100,200,300]]



print(s)


l=[1,2,3]
l=iter(l)
print(l)
print(next(l))
print(next(l))
print(next(l))



class TestIter(object):
    def __init__(self):
        self.age=20
    def __iter__(self):
        return self
    def __next__(self):
        if self.age<30:
            self.age+=1
            return self.age
        else:
            raise StopIteration
test=TestIter()
for age in test:
    print(age)


def getData(x):
    for i in [1,2,3,4]:
        yield i+x
f=getData(5)
for i in f:
    print(i)


for i in (x**2 for x in [1,2,3,4]):
    print(i)



import time

def calculateTime(func):
    print(func.__name__)
    def wrapper():
        starttime=time.time()
        func()
        starttime=time.time()-starttime
        print(starttime)
    return wrapper


@calculateTime
def test():
    print('test_func')
    time.sleep(1)


foo=calculateTime(test)
print(foo)
foo()

def paramMethod(flag=0):
    def calculateTime(func):
        def wrapper(*args):
            starttime=time.time()
            func(*args)
            starttime=time.time()-starttime
            print(starttime)
            print(flag)
        return wrapper
    return calculateTime
@paramMethod(flag=1)
def test(a,b):
    time.sleep(1)
    return a+b
print(test(1,2))

class Foo(object):
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        starttime=time.time()
        self.func()
        starttime=time.time()-starttime
        print(starttime)
@Foo
def test():
    print('test_func')
    time.sleep(1)
print(test)
print(test())















