#装饰器
'''
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，
我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用
'''
import time

def recordFuncInfo(func):
    print('start')
    print('函数名称:{}'.format(func.__name__))
    def execFunc(*args,**kwargs):
        return func(*args,**kwargs)
    print('over')
    return execFunc
def recordFuncInfo_2(func):
    print('start')
    print('函数名称:{}'.format(func.__name__))
    def execFunc(*args,**kwargs):
        return func(*args,**kwargs)
    print('over')
    return execFunc
@recordFuncInfo_2
@recordFuncInfo
def addData(*args):
    sl=list(args)
    if len(sl)==0:
        return 0
    else:
        count=0
        for i in sl:
            count+=i
        return count

if __name__ == '__main__':
    print(addData(1,2,3,4,5))
    print(addData.__name__)
    print(addData)



