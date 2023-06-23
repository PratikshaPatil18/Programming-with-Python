class A:
    pass
class B:
    def __repr__(self):
        return{1:'one',2:'two'}
a=A()
b=B()
print('from class A :',a)
print('from class B :',b.__repr__())
