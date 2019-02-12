try:
    a=5/2
except Exception:
    print('error')
else:
    print('no error')
finally:
    print('ok')

try:
    a=5/0
    print('no error')
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
else:
    print('no error')
finally:
    print('ok')

class MyError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


try:
    raise MyError
except MyError:
    print('Myerror')