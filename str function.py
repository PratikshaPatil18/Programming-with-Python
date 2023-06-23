class Base:
   pass
class Derived:
     def __str__(self):
        return('hello from Base class')
b=Base()
d=Derived()
print('message From class Base :',b)
print('message From class Derived :',d)
